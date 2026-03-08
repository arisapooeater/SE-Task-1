import requests # Must import requests so we can use API
import matplotlib
import pandas as pd
import numpy

# API Base URL for all world-wide countries
API_URL = "https://ponyapi.net/v1/character/all"

# Dictionary to store collected favourite characters
favlist = {}

def search_character(name):
    """Search for a MLP character by name and return its details.""" # Triple quotes is a docstring - allows multiline comments!
    response = requests.get(f"{API_URL}/{name.capitalize()}")
    if response.status_code == 200:
        data = response.json()[0]
        return {
            "name": data["name"],
            "region": data["region"],
            "population": data["population"],
        }
    
    else:
        print("Character not found.")
        return

def sort_characters():
    """Add a country to My Country List."""
    character = search_character(name)
    if character:
        favlist[character["name"]] = character
        print(f"{character['name']} added to Favourites List.")

def view_list():
    """Display all collected MLP characters."""
    if favlist:
        for name, details in favlist.items():
            print(f"{name} - capital: {details['capital']}, Region: {details['region']}, Population: {details['population']}, Languages: {details['languages']}, Flags: {details['flags']}")
    else:
        print("Your Favourites List is empty.")

def add_character():
    pass

def remove_character():
    pass