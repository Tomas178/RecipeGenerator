import pytest
from Models.RecipeGenerator import RecipeGenerator
from Enumerators.Filter import FilterEnum


@pytest.mark.parametrize("grocery_input", ["test", "apple, banana", ""])
def test_set_grocery_list(grocery_input):
    recipe_generator = RecipeGenerator(None)
    recipe_generator.set_grocery_list(grocery_input)
    assert recipe_generator.grocery_list == grocery_input


@pytest.mark.parametrize(
    "filter_type, filter_value",
    [
        (FilterEnum.CUISINE, "American"),
        (FilterEnum.DIET_TYPE, "Vegetarian"),
        (FilterEnum.PREPERATION_TIME, "30 minutes"),
    ],
)
def test_set_filter(filter_type, filter_value):
    recipe_generator = RecipeGenerator(None)
    recipe_generator.set_filter(filter_type, filter_value)
    assert recipe_generator.filters[filter_type] == filter_value
