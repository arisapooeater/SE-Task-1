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
        if c["name"] == name.title():
            return { #change formatting later
                "name": c["name"],
                "sex": c["sex"],
                "kind": c["kind"],
                "occupation": c["occupation"],
                "residence": c["residence"],
                "image": c["image"][0] if c["image"] else None
            }
    print("Character not found!")
    return 

def filter_characters():
    """Filter MLP characters by sex/kind and display to user."""

    response = requests.get(API_URL)

    if response.status_code != 200:
        print("API error.")
        return None
    
    characters = response.json()["data"]

    print("""
 ________________
| FILTER OPTIONS |
|----------------|
| 1. Sex         |
| 2. Kind        |
 ________________""")
    
    main_filter = input("""
Filter by (1/2): """).strip()
    
    if main_filter == "1":
        print("""
 ___________________
| SUBFILTER OPTIONS |
|-------------------|
| 1. Female         |
| 2. Male           |
 ___________________""")
        sub_filter = input("""
Filter by (1/2): """).strip()
        if sub_filter == "1":
            for c in characters:
                if c["sex"] == "Female":
                    print(c["name"])
        elif sub_filter == "2":
            for c in characters:
                if c["sex"] == "Male":
                    print(c["name"])
        else:
            print("Invalid input. Returning to main menu...")
    elif main_filter == "2":
        print("""
 ___________________
| SUBFILTER OPTIONS  |
|--------------------|
| 1. Pegasus         |
| 2. Unicorn         |
| 3. Earth Pony      |
| 4. Alicorn         |
| 5. Other creatures |
 ____________________""")
        sub_filter = input("""
Filter by (1/2/3/4/5): """).strip()
        if sub_filter == "1":
            for c in characters:
                if "Pegasus" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "2":
            for c in characters:
                if "Unicorn" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "3":
            for c in characters:
                if "Earth" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "4":
            for c in characters:
                if "Alicorn" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "5":
            for c in characters:
                if "Pegasus" not in c["kind"] and "Unicorn" not in c["kind"] and "Earth" not in c["kind"] and "Alicorn" not in c["kind"]:
                    print(f"{c['name']}: {c['kind']}")
        else:
            print("Invalid input. Enter a number between 1-5 (1/2/3/4/5). Returning to main menu...")
    else:
        print("Invalid input. Enter a number between 1-2 (1/2). Returning to main menu...")
    
def view_list(): 
    """Display all collected MLP characters in Favourites List and ask users if they want to add or remove characters."""
    exit = False
    empty = False
    while exit == False:
        if favlist:
            print("""
_____________________________________________________
FAVOURITES LIST""")
            for name, details in favlist.items():
                empty = False
                print(f"""
Name: {details['name']}
Sex: {details['sex']}
Kind: {details['kind']}
Occupation: {details['occupation']}
Residence: {details['residence']}
Image: {details['image']}
""") 
        else:
            empty = True
            print("""
_____________________________________________________
FAVOURITES LIST
                  
(empty)""")
        print("""
_____________________________________________________""")

        print("""
 _________________________
|         OPTIONS         |
|-------------------------|
| 1. Add character        |
| 2. Remove character     |
| 3. Exit Favourites List |
 _________________________""")
        user_input = input("""
Enter action (1/2/3): """).strip()
    
        if user_input == "1":
            add_character()
        elif user_input == "2":
            if empty == False:
                remove_character()
            else:
                print("Favourites List is empty. Action cannot be taken. Returning to Favourites List...")
        else:
            print("""
 ____________________________
| Exiting Favourites List... |
 ____________________________""")
            exit = True


def add_character(): 
    """Add characters to Favourites List"""
    name = input("""
What character would you like to add? (enter full name): """).title().strip()
    character = search_character(name) 
    if name in favlist:
        print("Character already in Favourites List! Returning to Favourites List...")
    elif character:
        favlist[character["name"]] = character
        print(f"""
 _____________________________________________________________________
| {name.capitalize()} added to Favourites List.                       
 _____________________________________________________________________""")
    else:
        print("Invalid input. Character not found")
    return
    

def remove_character(): 
    """Remove characters from Favourites List"""
    user_input = input("""
What character would you like to remove? (enter full name): """).title().strip()
    if user_input in favlist:
        favlist.pop(user_input)
        print(f"""
 _____________________________________________________________________
| {user_input} successfully removed!                                  |
 _____________________________________________________________________""")
    else:
        print("Character not found! Returning to favourites list...")
    return

#<------------------------------TEST YOUR FUNCTIONS BELOW----------------------------->

