import importlib


print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now THIS WILL RAISE AN UNCAUGHT EXCEPTION")

# This triggers the circular dependency and crashes the script
importlib.import_module("alchemy.grimoire.dark_spellbook")
