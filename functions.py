import requests # Must import requests so we can use API
import pandas as pd
from datetime import datetime
from term_image.image import from_url
import time
import os



# API Base URL for all MLP characters
API_URL = "https://ponyapi.net/v1/character/all"

# Dictionary to store collected favourite characters
favlist = {}

def search_character(name): #functioning
    """Search for a MLP character by name and return its details.""" # Triple quotes is a docstring - allows multiline comments!

    response = requests.get(API_URL)

    if response.status_code != 200:
        print("API error.")
        return 

    characters = response.json()["data"]

    # Search manually
    for c in characters:
        if c["name"] == name.title():
            return { #change formatting later
                "Name": c["name"],
                "Gender": c["sex"],
                "Kind": ", ".join(c["kind"]) if isinstance(c["kind"], list) else c["kind"],
                "Occupation": c["occupation"],
                "Residence": c["residence"],
                "Image": c["image"][0] if c["image"] else None
            }
    print("Character not found!")
    return 

def filter_characters():
    """Filter MLP characters by sex/kind and display to user."""

    response = requests.get(API_URL)

    if response.status_code != 200:
        print("API error.")
        return 
    
    characters = response.json()["data"]

    print("""
 ________________
| FILTER OPTIONS |
|----------------|
| 1. Sex         |
| 2. Kind        |
 ________________""")
    
    time.sleep(1)
    main_filter = input("""
Filter by (1/2): """).strip()
    time.sleep(1)
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
        time.sleep(1)
        if sub_filter == "1":
            print("""
FEMALE CHARACTERS""")
            for c in characters:
                if c["sex"] == "Female":
                    print(c["name"])
        elif sub_filter == "2":
            print("""
MALE CHARACTERS""")
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
        time.sleep(1)
        sub_filter = input("""
Filter by (1/2/3/4/5): """).strip()
        time.sleep(1)
        if sub_filter == "1":
            print("""
PEGASUS CHARACTERS""")
            for c in characters:
                if "Pegasus" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "2":
            print("""
UNICORN CHARACTERS""")
            for c in characters:
                if "Unicorn" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "3":
            print("""
EARTH PONY CHARACTERS""")
            for c in characters:
                if "Earth" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "4":
            print("""
ALICORN CHARACTERS""")
            for c in characters:
                if "Alicorn" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "5":
            print("""
OTHER CREATURES""")
            for c in characters:
                if "Pegasus" not in c["kind"] and "Unicorn" not in c["kind"] and "Earth" not in c["kind"] and "Alicorn" not in c["kind"]:
                    kind = ", ".join(c["kind"]) if isinstance(c["kind"], list) else c["kind"]
                    print(f"{c['name']}: {kind}")
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
Name: {details['Name']}
Sex: {details['Sex']}
Kind: {details['Kind']}
Occupation: {details['Occupation']}
Residence: {details['Residence']}
Image: {details['Image']}""")
        else:
            empty = True
            print("""
_____________________________________________________
FAVOURITES LIST
                  
(empty)""")
        print("""
_____________________________________________________""")
        time.sleep(1)
        print("""
 _________________________
|         OPTIONS         |
|-------------------------|
| 1. Add character        |
| 2. Remove character     |
| 3. Exit Favourites List |
 _________________________""")
        time.sleep(1)
        user_input = input("""
Enter action (1/2/3): """).strip()
        time.sleep(1)
        if user_input == "1":
            add_character()
        elif user_input == "2":
            if empty == False:
                remove_character()
            else:
                print("Favourites List is empty. Action cannot be taken. Returning to Favourites List...")
        elif user_input == "3":
            print("""
 ____________________________
| Exiting Favourites List... |
 ____________________________""")
            exit = True
        else:
            print("Invalid input. Enter a number between 1-3 (1/2/3). Returning to Favourites List...")
        time.sleep(2)


def add_character(): 
    """Add characters to Favourites List"""
    global log_df
    name = input("""
What character would you like to add? (enter full name): """).title().strip()
    character = search_character(name) 
    time.sleep(1)
    if name in favlist:
        print("Character already in Favourites List! Returning to Favourites List...")
    elif character:
        log_df.loc[len(log_df)] = ["add character", name]
        favlist[character["Name"]] = character
        print(f"""
 _____________________________________________________________________
| {name.capitalize()} added to Favourites List.                       
 _____________________________________________________________________""")
    else:
        print("Invalid input. Character not found")
    return
    

def remove_character(): 
    """Remove characters from Favourites List"""
    global log_df 
    name = input("""
What character would you like to remove? (enter full name): """).title().strip()
    time.sleep(1)
    if name in favlist:
        log_df.loc[len(log_df)] = ["remove character", name]
        favlist.pop(name)
        print(f"""
 _____________________________________________________________________
| {name} successfully removed!                                  
 _____________________________________________________________________""")
    else:
        print("Character not found! Returning to favourites list...")
    return

def record_actions(action, details=""):
    global log_df
    new_row = {
        "timestamp": datetime.now(),
        "action": action,
        "details": details
    }
    log_df.loc[len(log_df)] = new_row

#<------------------------------TEST YOUR FUNCTIONS BELOW----------------------------->


# Create an image instance from a file path
#image = from_url("https://vignette.wikia.nocookie.net/mlp/images/b/bc/Princess_Twilight_Sparkle_ID_S4E26.png")

# Display the image in the terminal
#image.draw()
