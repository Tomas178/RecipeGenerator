import pytest
from unittest import mock
from Helpers.app_helper import (
    select_mode,
    select_filter,
    select_cuisine,
    select_diet_type,
    select_preperation_time,
)
from Enumerators.Mode import ModeEnum
from Enumerators.Filter import FilterEnum
from Enumerators.Cuisine import CuisineEnum
from Enumerators.Diet_type import DietTypeEnum
from Enumerators.Preperation_time import PreperationTimeEnum


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("1\n", ModeEnum(1)),
        ("2\n", ModeEnum(2)),
        ("3\n", ModeEnum(3)),
        ("4\n", ModeEnum(4)),
        ("abc\n1\n", ModeEnum(1)),
        ("999\n2\n", ModeEnum(2)),
        ("123\n3\n", ModeEnum(3)),
        ("1ab2\n4\n", ModeEnum(4)),
    ],
)
def test_select_mode(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert select_mode() == expected_output


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("1\n", FilterEnum.CUISINE),
        ("2\n", FilterEnum.DIET_TYPE),
        ("3\n", FilterEnum.PREPERATION_TIME),
        ("4\n", FilterEnum.STOP_CHOOSING),
        ("abc\n1\n", FilterEnum.CUISINE),
        ("999\n2\n", FilterEnum.DIET_TYPE),
        ("123\n3\n", FilterEnum.PREPERATION_TIME),
        ("1ab2\n4\n", FilterEnum.STOP_CHOOSING),
    ],
)
def test_select_filter(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert select_filter() == expected_output


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("1\n", "American"),
        ("2\n", "Mexican"),
        ("3\n", "Italian"),
        ("4\n", "Lithuanian"),
        ("5\n", "None"),
        ("abc\n1\n", "American"),
        ("999\n2\n", "Mexican"),
        ("123\n3\n", "Italian"),
        ("1ab2\n4\n", "Lithuanian"),
        ("ABC\n5\n", "None"),
    ],
)
def test_select_cuisine(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert select_cuisine() == expected_output


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("1\n", "Vegan"),
        ("2\n", "Vegetarian"),
        ("3\n", "Keto"),
        ("4\n", "None"),
        ("abc\n1\n", "Vegan"),
        ("999\n2\n", "Vegetarian"),
        ("123\n3\n", "Keto"),
        ("1ab2\n4\n", "None"),
    ],
)
def test_select_diet_type(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert select_diet_type() == expected_output


@pytest.mark.parametrize(
    "user_input, expected_output",
    [
        ("1\n", "Quick"),
        ("2\n", "Moderate"),
        ("3\n", "Long"),
        ("4\n", "None"),
        ("abc\n1\n", "Quick"),
        ("999\n2\n", "Moderate"),
        ("123\n3\n", "Long"),
        ("1ab2\n4\n", "None"),
    ],
)
def test_select_preperation_time(user_input, expected_output):
    with mock.patch("builtins.input", side_effect=user_input.split("\n")):
        assert select_preperation_time() == expected_output
