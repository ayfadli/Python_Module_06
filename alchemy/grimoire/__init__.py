from .light_spellbook import light_spell_record
# Keep dark module out to avoid loading its intentional circular import.

__all__ = ["light_spell_record"]
