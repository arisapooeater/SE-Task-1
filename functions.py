import requests # Must import requests so we can use API
import pandas as pd
import numpy

# API Base URL for all MLP characters
API_URL = "https://ponyapi.net/v1/character/all"

# Dictionary to store collected favourite characters
favlist = {}

def search_character(name): #functioning
    """Search for a MLP character by name and return its details.""" # Triple quotes is a docstring - allows multiline comments!

    response = requests.get(API_URL)

    if response.status_code != 200:
        print("API error.")
        return None

    characters = response.json()["data"]

    # Search manually
    for c in characters:
        if c["name"].lower() == name.lower():
            return {
                "name": c["name"],
                "sex": c["sex"],
                "kind": c["kind"],
                "occupation": c["occupation"],
                "residence": c["residence"],
                "image": c["image"][0] if c["image"] else None
            }
    return ("Character not found.")

def filter_characters():
    """Filter MLP characters by sex/kind and display to user."""
    main_filter = input("""
FILTER OPTIONS
1. Sex 2.Kind """)
    
    if main_filter == "1":
        sub_filter = input("""
SUBFILTER OPTIONS
1. Female 2.Male""")
        if sub_filter == "1":
            pass
        elif sub_filter == "2":
            pass
        else:
            print("Invalid input. Returning to main menu...")
    elif main_filter == "2":
        sub_filter = input("""
SUBFILTER OPTIONS
1. """)
    else:
        pass

    
    print(search_character(filter)) #not functioning
    

def view_list(): #functioning
    """Display all collected MLP characters in Favourites List and ask users if they want to add or remove characters."""
    exit = False
    empty = False
    while exit == False:
        if favlist:
            for name, details in favlist.items():
                empty = False
                print(f"") #print name, sex, kind, occupation, residence, image
        else:
            empty = True
            print("""
FAVOURITES LIST
""")
        user_input = input("""
OPTIONS
1. Add character 
2. Remove character
3. Exit Favourites List""")
    
        if user_input == "1":
            add_character()
        elif user_input == "2":
            if empty == False:
                remove_character()
            else:
                print("Favourites List is empty.")
        else:
            print("Exiting Favourites List...")
            exit == True


def add_character(): 
    """Add characters to Favourites List"""
    user_input = input("What character would you like to add? (type full name): ")
    character = search_character(filter) # not functioning
    if character:
        favlist[character["name"]] = character
        print(f"{character['name']} added to Favourites List.")

def remove_character(): 
    """Remove characters from Favourites List"""
    user_input = input("What character would you like to remove? (type full name): ")
    if user_input in favlist():
        #del favlist(user_input)
        pass
    else:
        print("Character not found! Returning to favourites list...")

#<------------------------------TEST YOUR FUNCTIONS BELOW------------------------------>
