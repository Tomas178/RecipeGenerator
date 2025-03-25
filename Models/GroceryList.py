from dataclasses import dataclass
from Models.Ingredient import Ingredient


@dataclass
class GroceryList:
    """Represents a list of groceries"""

    _ingredients: list[Ingredient]

    def __init__(self, ingredients: list[Ingredient]):
        self._ingredients = ingredients if ingredients else []

    @property
    def ingredients(self) -> list[Ingredient]:
        """Getter for ingredients"""
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list[Ingredient]):
        """Setter for ingredients"""
        self._ingredients = ingredients

    def __str__(self) -> str:
        return "\n".join(str(ingredient) for ingredient in self.ingredients)
