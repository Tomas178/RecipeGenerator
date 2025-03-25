import base64
from Enumerators.Mode import ModeEnum
from Enumerators.Filter import FilterEnum
from Enumerators.Cuisine import CuisineEnum
from Enumerators.Diet_type import DietTypeEnum
from Enumerators.Preperation_time import PreperationTimeEnum


def select_mode() -> ModeEnum:
    """Displays the input menu to the user and returns selected mode."""

    print("Please select an option from the menu below:")
    for mode in ModeEnum:
        print(f"{mode.value}. {' '.join(mode.name.split('_')).capitalize()}")

    selected_mode = None
    while selected_mode == None:
        try:
            user_input = int(input("Enter a number: "))
            selected_mode = ModeEnum(user_input)
        except ValueError:
            print("Please enter a number.")
            continue
    print(f"\nSelected mode: {' '.join(selected_mode.name.split('_')).capitalize()}\n")
    return selected_mode


def select_filter() -> FilterEnum:
    """Displays the filter menu to the user and returns Filter type."""

    for filter in FilterEnum:
        print(f"{filter.value}. {' '.join(filter.name.split('_')).capitalize()}")

    selected_filter = None
    while selected_filter == None:
        try:
            user_input = int(input("Enter a number: "))
            selected_filter = FilterEnum(user_input)
        except ValueError:
            print("Please enter a number.")
            continue
    print(
        f"\nSelected filter: {' '.join(selected_filter.name.split('_')).capitalize()}\n"
    )
    return selected_filter


def encode_image(image_path: str) -> str:
    """Encodes an image file to a Base64 string."""

    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"Image Path: {image_path} not found.")
        return ""


def select_cuisine() -> str:
    """Displays the cuisine menu to the user and returns selected cuisine."""

    for cuisine in CuisineEnum:
        print(f"{cuisine.value}. {' '.join(cuisine.name.split('_')).capitalize()}")

    selected_cuisine = None
    while selected_cuisine == None:
        try:
            user_input = int(input("Enter a number: "))
            selected_cuisine = CuisineEnum(user_input)
        except ValueError:
            print("Please enter a number.")
            continue
    print(
        f"\nSelected cuisine: {' '.join(selected_cuisine.name.split('_')).capitalize()}\n"
    )
    return selected_cuisine.name.capitalize()


def select_diet_type() -> str:
    """Displays the diet type menu to the user and returns selected diet type."""

    for diet_type in DietTypeEnum:
        print(f"{diet_type.value}. {' '.join(diet_type.name.split('_')).capitalize()}")

    selected_diet_type = None
    while selected_diet_type == None:
        try:
            user_input = int(input("Enter a number: "))
            selected_diet_type = DietTypeEnum(user_input)
        except ValueError:
            print("Please enter a number.")
            continue
    print(
        f"\nSelected diet type: {' '.join(selected_diet_type.name.split('_')).capitalize()}\n"
    )
    return selected_diet_type.name.capitalize()


def select_preperation_time() -> str:
    """Displays the preperation time menu to the user and returns selected preperation time."""

    for preperation_time in PreperationTimeEnum:
        print(
            f"{preperation_time.value}. {' '.join(preperation_time.name.split('_')).capitalize()}"
        )

    selected_preperation_time = None
    while selected_preperation_time == None:
        try:
            user_input = int(input("Enter a number: "))
            selected_preperation_time = PreperationTimeEnum(user_input)
        except ValueError:
            print("Please enter a number.")
            continue
    print(
        f"\nSelected preperation time: {' '.join(selected_preperation_time.name.split('_')).capitalize()}\n"
    )
    return selected_preperation_time.name.capitalize()
