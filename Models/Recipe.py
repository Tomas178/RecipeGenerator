from dataclasses import dataclass
from Models.GroceryList import GroceryList


@dataclass
class Recipe:
    _name: str
    _ingredients: GroceryList
    _instructions: list[str]

    def __init__(self, name: str, ingredients: GroceryList, instructions: list[str]):
        self._name = name
        self._ingredients = ingredients
        self._instructions = instructions

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def ingredients(self) -> GroceryList:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: GroceryList):
        self._ingredients = ingredients

    @property
    def instructions(self) -> list[str]:
        return self._instructions

    @instructions.setter
    def instructions(self, instructions: list[str]):
        self._instructions = instructions

    def __str__(self) -> str:
        instructions_str = "\n".join(self._instructions)
        return f"Name: {self._name}\nIngredients: {self._ingredients}\nInstructions: {instructions_str}"
