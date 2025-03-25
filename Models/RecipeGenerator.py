from openai import OpenAI
from Models.GroceryList import GroceryList
from Models.Recipe import Recipe
from Enumerators.Filter import FilterEnum
from Helpers import OpenAI_helper


class RecipeGenerator:
    def __init__(self, client: OpenAI):
        """Initializes the RecipeGenerator."""

        self.client = client
        self.grocery_list = GroceryList([])
        self.filters = {
            FilterEnum.CUISINE: "Whatever",
            FilterEnum.DIET_TYPE: "Whatever",
            FilterEnum.PREPERATION_TIME: "Whatever",
        }

    def set_grocery_list(self, grocery_list: GroceryList):
        """Sets the grocery list based on user input (manual, image, or CSV)."""

        self.grocery_list = grocery_list

    def set_filter(self, filter_type: FilterEnum, value: str):
        """Applies a filter based on user selection."""

        if filter_type in self.filters:
            self.filters[filter_type] = value

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

    def __str__(self):
        return f"Grocery List:\n{self.grocery_list}\nFilters:\n{self.filters}"
