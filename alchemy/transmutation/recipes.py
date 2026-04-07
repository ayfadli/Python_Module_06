# Absolute import (starting from the root directory)
from elements import create_fire

# Relative imports (going up one level into the alchemy package)
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' and "
        f"'{strength_potion()}' mixed with '{create_fire()}'"
    )
