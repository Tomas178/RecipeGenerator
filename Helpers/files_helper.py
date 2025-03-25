import csv
import os
from Models.GroceryList import GroceryList
from Models.Recipe import Recipe
from Models.Ingredient import Ingredient

RECIPES_FOLDER_PATH = "Recipes/"


def get_GroceryList(csv_file_path: str) -> GroceryList:
    """Returns GroceryList from a CSV file."""

    ingredient_list = []
    try:
        with open(csv_file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                ingredient_list.append(Ingredient(row[0]))
    except FileNotFoundError:
        print("Failed to open the file!")

    return GroceryList(ingredient_list)


def save_recipe(recipe: Recipe) -> None:
    """Saves recipe to a TXT file."""

    recipe_name: str = recipe.name
    recipe_ingredients: list[Ingredient] = recipe.ingredients.ingredients
    recipe_instructions: list[str] = recipe.instructions

    validate_Recipes_folder()
    if not recipe_exists(recipe_name):
        with open(
            f"{RECIPES_FOLDER_PATH}{recipe_name}.txt",
            mode="w",
            newline="",
            encoding="utf-8",
        ) as file:
            file.write(f"Recipe Name: {recipe_name}\n")
            file.write("Ingredients:\n")
            for i, ingredient in enumerate(recipe_ingredients, start=1):
                file.write(f"\t{i}. {ingredient.name}\n")

            file.write("Instructions:\n")
            for i, instruction in enumerate(recipe_instructions, start=1):
                file.write(f"\t{i}. {instruction}\n")
    else:
        print(f"Recipe {recipe_name} already exists.")


def validate_Recipes_folder() -> None:
    """Validates Recipe folder."""

    if not os.path.exists(RECIPES_FOLDER_PATH):
        os.makedirs(RECIPES_FOLDER_PATH)


def recipe_exists(recipe_name: str) -> bool:
    """Checks if a recipe with given name already exists."""

    return os.path.exists(f"{RECIPES_FOLDER_PATH}{recipe_name}.csv")
