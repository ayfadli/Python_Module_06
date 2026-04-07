from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    ing_lower = ingredients.lower()

    # Check if any allowed ingredient is in the submitted string
    if any(item in ing_lower for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
