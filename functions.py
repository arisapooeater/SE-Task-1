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

# Storing the help message
help_text = """
 ___________________________________________________________________________________________________________
|                                    HELP !! Answering Common Questions                                     |
|-----------------------------------------------------------------------------------------------------------|
| 1. Why does the system keep saying my input is invalid?                                                   |
|    --> You need to respond with the NUMBER of your chosen action when you are given a list of options     |
|    --> Remember to spell any names you type with correct spelling or the system will not process it!      |
|                                                                                                           |
| 2. Why does the system keep saying "API Error."?                                                          |
|    --> If the system is responding with "API Error.", that means the request made to our information      |
|        source was unsuccessful and there is a problem somewhere!                                          |
|    --> In this case, please contact arisa.komatsu@education.nsw.gov.au and notify me on the error so it   |
|        can be fixed ASAP :)                                                                               |
|                                                                                                           |
| 3. What is the Favourites List and how can I use it?                                                      |
|    --> The Favourites List is a personal list you can create of all your favourite MLP characters!        |
|    --> You can add and remove characters to your liking and it will store and display their general       |
|        character information.                                                                             |
|    --> It can be used for comparing the stats on characters, or just collecting your MLP biases!          |
|    --> The Favourites List loops until your satisfied with the list you've created, in which you can      |   
|        select the exit option to return to the Main Menu and continue interacting with the system!        |
|                                                                                                           |
| 4. What is the user interactions log?                                                                     |
|    --> The user interactions log is a local record of all the interactions YOU as the user have made      |
|        with our system.                                                                                   |
|    --> You can view what you've done on our application within the runtime session                        |
|    --> Don't worry, no personal information is retrieved and all data is cleared after each runtime       |
|        session!                                                                                           |
|-----------------------------------------------------------------------------------------------------------|
|                                                                                                           |
| For further help with navigating the MLP Character Guide or if you have a "ModuleNotFoundError", please   |
|                          go to the README file for a more intensive explanation !                         |
|                                                                                                           |
 ___________________________________________________________________________________________________________"""

def search_character(name): 
    """Search for a MLP character by name and return its details.""" # Triple quotes is a docstring - allows multiline comments!

    # Sends request to retrieve all data from API
    response = requests.get(API_URL)
    
    # Send error message to user if API is not functioning
    if response.status_code != 200:
        print("API error.")
        return 

    characters = response.json()["data"]

    # Search manually for data that matches "name" and returns the character's data to the main function
    for c in characters:
        if c["name"] == name.title():
            return { 
                "Name": c["name"],
                "Gender": c["sex"],
                "Kind": ", ".join(c["kind"]) if isinstance(c["kind"], list) else c["kind"],
                "Occupation": c["occupation"],
                "Residence": c["residence"],
                "Image":  c["image"][0] if c["image"] else None
            }
    print("Character not found! Returning to main menu...") # Display user input error message
    return 

def filter_characters(log_df):
    """Filter MLP characters by sex/kind and display to user."""

    # Sends request to retrieve data from API
    response = requests.get(API_URL)

    # Send error message to user if API is not functioning and retrieval is not possible
    if response.status_code != 200:
        print("API error.")
        return 
    
    # Retrieve data from API
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
            # If characters in the data retrieved from API are female, the character's name is displayed to user
            for c in characters:
                if c["sex"] == "Female":
                    print(c["name"])
        elif sub_filter == "2":
            print("""
MALE CHARACTERS""")
            # If characters in the data retrieved from API are male, the character's name is displayed to user
            for c in characters:
                if c["sex"] == "Male":
                    print(c["name"])
        elif sub_filter == 'h':
            print(help_text)
        else:
            print("Invalid input. Returning to main menu...") # Display user input error message
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
            # If characters in the data retrieved from API is a Pegasus, the character's name is displayed to user
            for c in characters:
                if "Pegasus" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "2":
            print("""
UNICORN CHARACTERS""")
            # If characters in the data retrieved from API is a Unicorn, the character's name is displayed to user
            for c in characters:
                if "Unicorn" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "3":
            print("""
EARTH PONY CHARACTERS""")
            # If characters in the data retrieved from API is an Earth Pony, the character's name is displayed to user
            for c in characters:
                if "Earth" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "4":
            print("""
ALICORN CHARACTERS""")
            # If characters in the data retrieved from API is an Alicorn, the character's name is displayed to user
            for c in characters:
                if "Alicorn" in c["kind"]:
                    print(c["name"])
        elif sub_filter == "5":
            print("""
OTHER CREATURES""")
            # If characters in the data retrieved from API is not any of the above kinds, the character's name and kind is displayed to user
            for c in characters:
                if "Pegasus" not in c["kind"] and "Unicorn" not in c["kind"] and "Earth" not in c["kind"] and "Alicorn" not in c["kind"]:
                    kind = ", ".join(c["kind"]) if isinstance(c["kind"], list) else c["kind"]
                    print(f"{c['name']}: {kind}")
        elif sub_filter.lower() == 'h':
            print(help_text)
        else:
            print("Invalid input. Enter a number between 1-5 (1/2/3/4/5). Returning to main menu...") # Display user input error message
        
    elif main_filter.lower() == 'h':
        print(help_text)
    else:
        print("Invalid input. Enter a number between 1-2 (1/2). Returning to main menu...") # Display user input error message
    # Record user interaction in log_df
    record_actions(log_df, "remove character", sub_filter)
    
def view_list(log_df): 
    """Display all collected MLP characters in Favourites List and ask users if they want to add or remove characters."""
    exit = False
    empty = False
    # Loop displaying favlist and adding/removing characters until user selects exit Favourites List
    while exit == False:
        # Check favlist is not empty
        if favlist:
            print("""
_____________________________________________________
FAVOURITES LIST""")
            for name, details in favlist.items(): # Display the name, gender, kind, occupation, residence of all characters in favlist
                empty = False
                print(f"""
Name: {details['Name']}
Gender: {details['Gender']}
Kind: {details['Kind']}
Occupation: {details['Occupation']}
Residence: {details['Residence']}""")
                if details['Image']: # Check there's a value in 'Image' 
                    display_image(details["Image"]) # Call display_image() function to visualise image in terminal
        else: # Display empty favlist
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
|     FAVLIST OPTIONS     |
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
            add_character(log_df) # Call add_character() function
            clear_screen("Favourites List")
        elif user_input == "2":
            if empty == False: # Check favlist wasn't empty
                remove_character(log_df) # Call remove_character() function
                clear_screen("Favourites List")
            else:
                print("Favourites List is empty. Action cannot be taken. Returning to Favourites List...") # Display error message as there are no characters available to remove from favlist
                os.system('cls')
        elif user_input == "3":
            print("""
 ____________________________
| Exiting Favourites List... |
 ____________________________""")
            exit = True # Break while loop and return to main menu loop
            os.system('cls')
        elif user_input.lower() == 'h':
            print(help_text)
        else:
            print("Invalid input. Enter a number between 1-3 (1/2/3). Returning to Favourites List...") # Display user input error message
        time.sleep(2)


def add_character(log_df): 
    """Add characters to Favourites List"""
    name = input("""
What character would you like to add? (enter full name): """).title().strip()
    # Get character data that matches name (user input)
    character = search_character(name) 
    time.sleep(1)
    # Check if character is already in favlist
    if name in favlist:
        print("Character already in Favourites List! Returning to Favourites List...")
    # Check character exists in API and search_character() returned a value
    elif character:
        # Record user interaction in log_df
        record_actions(log_df,"add character", name)

        # Add character to favlist
        favlist[character["Name"]] = character
        print(f"""
 _____________________________________________________________________
| {name.title()} added to Favourites List.                       
 _____________________________________________________________________""")
    elif name.lower() == 'h':
        print(help_text)
    else:
        print("Character not found! Returning to Favourites List...") # Display user input error message
    return
    

def remove_character(log_df): 
    """Remove characters from Favourites List"""
    name = input("""
What character would you like to remove? (enter full name): """).title().strip()
    time.sleep(1)
    if name in favlist:
        # Record user interaction in log_df
        record_actions(log_df, "remove character", name)

        # Remove character from favlist
        favlist.pop(name)
        print(f"""
 _____________________________________________________________________
| {name.title()} successfully removed!                                  
 _____________________________________________________________________""")
    elif name.lower() == 'h':
        print(help_text)
    else:
        print("Character not found! Returning to Favourites List...")  # Display user input error message
    return

def record_actions(log_df, action, details=""):
    """Record user interactions in a dictionary"""
    # Add new row to log_df with timestamp, action, and details (user input)
    log_df.loc[len(log_df)] = [
        datetime.now(),
        action,
        details
    ]

def display_image(url):
    """Display character image in terminal"""
    # Remove "/revision/latest?cb=..." from image URL as its not compatible with image.draw()
    fixed_url = url.split("/revision")[0]

    # Create an image instance from a file path
    image = from_url(fixed_url)

    # Display the image in the terminal
    image.draw()
    return


def clear_screen(menu):
    """Clear terminal when user is done with an action"""
    clear = ''
    while clear != 'yes': # Loop the question until user enters 'yes'
        time.sleep(0.5)
        clear = input(f"""
Once you're ready to return to {menu}, enter 'yes': """).strip().lower() # Change {menu} depending on action and loop the user is in (eg. Favourites List, Main Menu)
        if clear == 'yes':
            clear = 'yes'
            os.system('cls') # Clear screen
            time.sleep(1)
            return
        else:
            time.sleep(0.5)
            print("Invalid input! Please try again.") # Display user input error message