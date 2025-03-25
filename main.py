from dotenv import load_dotenv
from openai import OpenAI
from Helpers import api_helper
from Helpers import user_input_helper
from Helpers import app_helper
from Helpers import OpenAI_helper
from Helpers import files_helper
from Enumerators.Mode import ModeEnum
from Enumerators.Filter import FilterEnum
from Models.GroceryList import GroceryList
from Models.RecipeGenerator import RecipeGenerator

load_dotenv()

AVAILABLE_IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".gif")


def main():
    print("Welcome to the Recipe Generator!")
    api_helper.is_valid_APIs()
    client = OpenAI()
    recipe_generator = RecipeGenerator(client)

    while True:
        try:
            mode = app_helper.select_mode()

            match mode:
                case ModeEnum.MANUAL_INPUT:
                    recipe_generator.set_grocery_list(
                        user_input_helper.ask_user_for_ingredients()
                    )
                case ModeEnum.IMAGE_INPUT:
                    image_path = user_input_helper.ask_user_for_image_path(
                        AVAILABLE_IMAGE_EXTENSIONS
                    )
                    if image_path != "q":
                        base64_image = app_helper.encode_image(image_path)
                        grocery_list = OpenAI_helper.get_AI_response_from_image(
                            client, base64_image
                        )
                        print(grocery_list)
                        recipe_generator.set_grocery_list(grocery_list)
                case ModeEnum.CSV_INPUT:
                    csv_file_path = user_input_helper.ask_user_for_csv_path()
                    if csv_file_path != "q":
                        grocery_list = files_helper.get_GroceryList(csv_file_path)
                        recipe_generator.set_grocery_list(grocery_list)
                case ModeEnum.EXIT:
                    print("Exiting program.")
                    break

            while True:
                selected_filter = app_helper.select_filter()
                if selected_filter == FilterEnum.STOP_CHOOSING:
                    break
                value = None
                match selected_filter:
                    case FilterEnum.CUISINE:
                        value = app_helper.select_cuisine()
                    case FilterEnum.DIET_TYPE:
                        value = app_helper.select_diet_type()
                    case FilterEnum.PREPERATION_TIME:
                        value = app_helper.select_preperation_time()

                if value:
                    recipe_generator.set_filter(selected_filter, value)

            recipe = recipe_generator.generate_recipe()
            if recipe:
                print(f"Recipe name: {recipe.name}")
                shopping_list = recipe_generator.get_shopping_list(recipe)
                if shopping_list.ingredients:
                    print("\nYou are missing these ingredients:")
                    print(shopping_list)

                if user_input_helper.ask_user_to_save_recipe():
                    files_helper.save_recipe(recipe)

        except KeyboardInterrupt:
            print("\nExiting program.")
            break


if __name__ == "__main__":
    main()
