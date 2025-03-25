import pytest
from unittest import mock
from Helpers.user_input_helper import (
    ask_user_for_ingredients,
    ask_user_for_ingredient,
    ask_user_for_another_ingredient,
    ask_user_to_save_recipe,
)
from Models.Ingredient import Ingredient
from Models.GroceryList import GroceryList


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        (
            "Tomato\ny\nCucumber\nN",
            GroceryList([Ingredient("Tomato"), Ingredient("Cucumber")]),
        ),
    ],
)
def test_ask_user_for_ingredients(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert ask_user_for_ingredients() == expected_output


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("Tomato\n", Ingredient("Tomato")),
        ("  Cucumber   \n", Ingredient("Cucumber")),
        ("\n \nTomato \n", Ingredient("Tomato")),
    ],
)
def test_ask_user_for_ingredient(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert ask_user_for_ingredient() == expected_output


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("Y\n", True),
        ("y\n", True),
        ("n  \n", False),
        ("  N  \n", False),
        ("g\n  Y \n", True),
        (" t \n N  \n", False),
    ],
)
def test_ask_user_to_save_recipe(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert ask_user_for_another_ingredient() == expected_output


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("Y\n", True),
        ("y\n", True),
        ("n  \n", False),
        ("  N  \n", False),
        ("g\n  Y \n", True),
        (" t \n N  \n", False),
    ],
)
def test_ask_user_to_save_recipe(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert ask_user_to_save_recipe() == expected_output
