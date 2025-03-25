from dataclasses import dataclass


@dataclass
class Ingredient:
    """Represents a single ingredient"""

    _name: str

    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return self._name

    @property
    def name(self):
        return self._name
