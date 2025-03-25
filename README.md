# Smart Recipe Generator

## Description: A CLI app that suggests recipes based on available ingredients.

### Features:
        1. Users enter ingredients they have at home or input an image or CSV file.
        2. Filter by cuisine, diet type, or preparation time.
        3. AI suggests recipes using those ingredients and Selected filter.
        4. Generate a shopping list for missing ingredients.

## Enumerators
<details>
<summary><strong>ModeEnum</strong></summary>

### Description
The `ModeEnum` enumerator defines available modes for entering ingredients.

### Values

- **MANUAL_INPUT** – Allows the user to enter ingredients manually.
- **IMAGE_INPUT** – Allows the user to provide an image from which ingredients are extracted.
- **FILE_INPUT** – Allows the user to provide a .csv file from which ingredients are read.
- **EXIT** – Allows the user to exit the Recipe generator app.
</details>

<details>
<summary><strong>FilterEnum</strong></summary>

### Description
The `FilterEnum` enumerator defines available filtering types.

### Values

- **CUISINE** – Allows the user to select from available cuisines.
- **DIET_TYPE** – Allows the user to select from available diet types.
- **PREPERATION_TIME** – Allows the user to select from available preperation times.
- **STOP_CHOOSING** – Allows the user to stop choosing filtering types.
</details>

<details>
<summary><strong>CuisineEnum</strong></summary>

### Description
The `CuisineEnum` enumerator defines available Cuisines in the app.

### Values

- **AMERICAN** – Sets the Cuisine value to be American.
- **MEXICAN** – Sets the Cuisine value to be Mexican.
- **ITALIAN** – Sets the Cuisine value to be Italian.
- **LITHUANIAN** – Sets the Cuisine value to be Lithuanian.
- **NONE** - Sets the Cuisine value to be None.
</details>

<details>
<summary><strong>DietTypeEnum</strong></summary>

### Description
The `DietTypeEnum` enumerator defines available diet types in the app.

### Values

- **VEGAN** – Sets the Diet Type value to be Vegan.
- **VEGETARIAN** – Sets the Diet Type value to be Vegetarian.
- **KETO** – Sets the Diet Type value to be Keto.
- **NONE** - Sets the Diet Type value to be None.
</details>

<details>
<summary><strong>PreperationTimeEnum</strong></summary>

### Description
The `PreperationTimeEnum` enumerator defines available preperation times in the app.

### Values

- **QUICK** – Sets the Preperation Time value to be Quick.
- **MODERATE** – Sets the Preperation Time value to be Moderate.
- **LONG** – Sets the Preperation Time value to be Long.
- **NONE** - Sets the Preperation Time value to be None.
</details>

## Models
<details>
<summary><strong>Ingredient</strong></summary>

### Data
- **name** – Name of the ingredient.

</details>

<details>
<summary><strong>GroceryList</strong></summary>

### Data
- **ingredients** – list of ingredients from Ingredient class.

</details>

<details>
<summary><strong>Recipe</strong></summary>

### Data
- **name** – Name of the recipe.
- **ingredients** – a GroceryList class.
- **instructions** - a list of strings that is an individual step in instructions.

</details>

<details>
<summary><strong>RecipeGenerator</strong></summary>

### Data
- **client** – An OpenAI object.
- **grocery_list** – a GroceryList class.
- **filters** - a dictionary of FilterEnum and its value.

<details>
<summary><strong>Methods</strong></summary>

1. Setter for grocery list:
```python
def set_grocery_list(self, grocery_list: GroceryList):
    """Sets the grocery list based on user input (manual, image, or CSV)."""

    self.grocery_list = grocery_list
```

2. Setter for filters:
```python
def set_filter(self, filter_type: FilterEnum, value: str):
    """Applies a filter based on user selection."""

    if filter_type in self.filters:
        self.filters[filter_type] = value
```

3. Generate recipe based on grocery list and filters:
```python
def generate_recipe(self) -> Recipe:
    """Uses OpenAI to generate a recipe based on current ingredients and filters."""

    try:
        recipe = OpenAI_helper.get_AI_response_for_recipe(
            self.client,
            self.grocery_list,
            self.filters[FilterEnum.CUISINE],
            self.filters[FilterEnum.DIET_TYPE],
            self.filters[FilterEnum.PREPERATION_TIME],
        )
        return recipe
    except IndexError:
        print("AI failed to generate a valid recipe! Please try again.")
        return None
```

4. A method to get missing ingredients list for the generated recipe:
```python
def get_shopping_list(self, recipe: Recipe) -> GroceryList:
    """
    Compares the generated recipe's ingredients with the user's available ingredients
    and returns a grocery list of missing ingredients.
    """
    missing_ingredients = [
        ingredient
        for ingredient in recipe.ingredients.ingredients
        if ingredient not in self.grocery_list.ingredients
    ]
    return GroceryList(missing_ingredients)
```
</details>
</details>

### Helpers

<details>
<summary><strong>api_helper</strong></summary>

### Description
The `api_helper` module is created for checking API keys.

<details>
<summary><strong>Functions</strong></summary>

1. Checks if the APIs are set in the .env file:
```python 
def is_valid_APIs() -> None:
```

2. All these functions below check for an API key based on their variable name:
```python
def check_OpenAI_API_key() -> None:
def check_rapid_API_key() -> None:
def check_OpenAI_org_id() -> None:
def check_OpenAI_project_id() -> None:
```
</details>
</details>

<details>
<summary><strong>app_helper</strong></summary>

### Description
The `app_helper` module is created for handling user inputs when selecting ingredient input type and filtering choices.

<details>
<summary><strong>Functions</strong></summary>

```python
def select_mode() -> ModeEnum:
    """Displays the input menu to the user and returns selected mode."""
def select_filter() -> FilterEnum:
    """Displays the filter menu to the user and returns Filter type."""
def encode_image(image_path: str) -> str:
    """Encodes an image file to a Base64 string."""
def select_cuisine() -> str:
    """Displays the cuisine menu to the user and returns selected cuisine."""
def select_diet_type() -> str:
    """Displays the diet type menu to the user and returns selected diet type."""
def select_preperation_time() -> str:
    """Displays the preperation time menu to the user and returns selected preperation time."""
```
</details>
</details>

<details>
<summary><strong>files_helper</strong></summary>

### Description
The `files_helper` module is created for handling the reading, writing, and validating of files.

<details>
<summary><strong>Functions</strong></summary>

```python
def get_GroceryList(csv_file_path: str) -> GroceryList:
    """Returns GroceryList from a CSV file."""
def save_recipe(recipe: Recipe) -> None:
    """Saves recipe to a TXT file."""
def validate_Recipes_folder() -> None:
    """Validates Recipe folder."""
def recipe_exists(recipe_name: str) -> bool:
    """Checks if a recipe with given name already exists."""
```
</details>
</details>

<details>
<summary><strong>OpenAI_helper</strong></summary>

### Description
The `OpenAI_helper` module is created for handling the requests to OpenAI and responses from OpenAI.

<details>
<summary><strong>Functions</strong></summary>

```python
def get_AI_response_from_image(client: OpenAI, base64_image: str) -> GroceryList:
    """Sends an image to OpenAI API and returns the AI response."""
def get_AI_response_for_recipe(
    client: OpenAI,
    groceryList: GroceryList,
    cuisine: str,
    diet_type: str,
    preparation_time: str,
) -> Optional[Recipe]:
    """Sends ingredients and filtering choices to OpenAI API and returns the AI generated recipe."""
```
</details>
</details>

<details>
<summary><strong>user_input_helper</strong></summary>

### Description
The `user_input_helper` module is created for handling the user inputs when entering ingredients and files paths.

### Data
```python 
AVAILABLE_IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".gif")
```

<details>
<summary><strong>Functions</strong></summary>

```python
def ask_user_for_ingredients() -> GroceryList:
    """Returns a list of ingredients (GroceryList class)."""
def ask_user_for_ingredient() -> Ingredient:
    """Asks and returns a single ingredient."""
def ask_user_for_another_ingredient() -> bool:
    """Asks user if they want to enter another ingredient and returns boolean value."""
def ask_user_for_image_path(AVAILABLE_IMAGE_EXTENSIONS: tuple[str]) -> str:
    """Asks user the image path returns the image path."""
def ask_user_for_csv_path() -> str:
    """Asks the user CSV file path returns the CSV file path."""
def ask_user_to_save_recipe() -> bool:
    """Asks user if they want to save recipe and returns boolean value."""
```
</details>
</details>

### CSV file structure

```csv
Tomato
Apple
Cucumber
Broccoli
Orange
Eggs
Meat
Yogurt
```

### Available formats for image input – .png, .jpg, .jpeg, .webp, .gif

[Back to top](#readme)
