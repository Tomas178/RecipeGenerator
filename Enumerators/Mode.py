from enum import Enum


class ModeEnum(Enum):
    """Enumerator for menu choices"""

    MANUAL_INPUT = 1
    IMAGE_INPUT = 2
    CSV_INPUT = 3
    EXIT = 4
