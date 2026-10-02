from alchemy.elements import create_air
from elements import create_fire
from ..potions import strength_potion


def lead_to_gold() -> str:
    air = create_air()
    strength = strength_potion()
    fire = create_fire()
    recipe = f"brew '{air}' and '{strength}' mixed with '{fire}'"
    return (f"Recipe transmuting Lead to Gold: {recipe}")