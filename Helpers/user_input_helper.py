import os
from Models.GroceryList import GroceryList
from Models.Ingredient import Ingredient


def ask_user_for_ingredients() -> GroceryList:
    """Returns a list of ingredients (GroceryList class)."""

    ingredient_list = []
    while True:
        ingredient: Ingredient = ask_user_for_ingredient()
        ingredient_list.append(ingredient)
        if not ask_user_for_another_ingredient():
            break

    return GroceryList(ingredient_list)


def ask_user_for_ingredient() -> Ingredient:
    """Asks and returns a single ingredient."""

    while True:
        ingredient = input("Enter an ingredient: ").strip()
        if ingredient:
            return Ingredient(ingredient)
        else:
            print("Please enter an ingredient.")


def ask_user_for_another_ingredient() -> bool:
    """Asks user if they want to enter another ingredient and returns boolean value."""

    while True:
        answer = (
            input("Would you like to add another ingredient? (y/n): ").strip().lower()
        )
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")


def ask_user_for_image_path(AVAILABLE_IMAGE_EXTENSIONS: tuple[str]) -> str:
    """Asks user for image path and returns the image path."""

    while True:
        image_path = input("Enter the path to the image (enter 'q' to quit): ").strip()
        if image_path.lower() == "q":
            return image_path
        elif not image_path.endswith(AVAILABLE_IMAGE_EXTENSIONS):
            print(
                "Wrong image extension! Allowed extensions: .png, .jpg, .jpeg, .webp, .gif"
            )
        elif not os.path.exists(image_path):
            print("This image does not exist!")
        else:
            return image_path


def ask_user_for_csv_path() -> str:
    """Asks the user for CSV file path and returns the CSV file path."""

    while True:
        csv_file_path = input(
            "Enter the path to CSV file (enter 'q' to quit): "
        ).strip()
        if csv_file_path.lower() == "q":
            return csv_file_path
        elif not csv_file_path.endswith(".csv"):
            print("Wrong file extension! File should end with .csv")
        elif not os.path.exists(csv_file_path):
            print("This CSV file does not exist!")
        else:
            return csv_file_path


def ask_user_to_save_recipe() -> bool:
    """Asks user if they want to save recipe and returns boolean value."""

    while True:
        user_answer = (
            input("Would you like to save this recipe? (y/n): ").strip().lower()
        )
        if user_answer == "y":
            return True
        elif user_answer == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")
