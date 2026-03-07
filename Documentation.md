# MLP: Character Guide Application (Development Process)
Arisa Komatsu
## Requirements Definition
### Objective
To enable users to search for and sort characters in the animated series 'My Little Pony' by either gender or kind, providing general information on character traits like their alias, residence, occupation etc. This application aims to make MLP lore and information more readily available for the fandom without the need of constant web surfing.

### Functional Requirements
- **User Interface:** Should provide users with a list of action options with a textfield for users to enter their choice/input. 
- **Data Retrieval/Display:** System should be able to pull data from API and return it based on user commands. Users should be able to access character names, gender, residence, occupation and a profile image of all characters in My Little Pony.
- **User interaction:** System should allow users to search for characters by name, type or gender and create a personal collection of favourite characters.
- **Error processing:** System should be able to identify invalid inputs and respond with accurate and specific error messages.

### Non-Functional Requirements
- **Performance:** System should respond to user input quickly within 3 seconds and shouldn't bug out from invalid inputs or errors.
- **Usability:** System should be structured and clearly accessible for all users. The README file should also provide extensive assistance on using and navigating the project.
- **Reliability:** The API chosen for this project should contain accurate, reliable data on the My Little Pony Universe. Additionally, the system should be able to relay this data without faults. 
- **Security:** API key should be hidden to prevent data theft and unauthorised access. Should practise data minimisation.
- **Accessibility:** System should be easily navigated and usable for a range of abilities. README file should be able to explain how to use the system clearly and concisely.

## Determining Specification
### Functional Specifications
### Non-Functional Specifications
**Wording of messages:** 

Overall tone of system messages and menu should be very friendly and catering to the user and must maintain a warm character while giving clear and readable responses. 

**Main Menu:** 

Main menu should be both well structured and aesthetically pleasing with small embellishments to lean into the fantasy genre of My Little Pony. The menu options should be cleary visible, and easy to select. Users should be able to select their option easily with an understanding of what the option does and what results they should expect.

**Frames:** 

System messages and menus should be enclosed in a box with visual structure, whereas user input fields should have a line above and below for emphasis.

**Timing:**

 All system actions (eg. loading main menu, printing search results etc.) should occur within 2-3 seconds and navigating the project should feel natural and streamlined to users.

**Clearing screen:**

 After the system completes a user action, it should ask the user if they are done to clear the screen and reload the main menu for further actions and prevent a cluttered and confusing interface.

## Design
### Structure Chart
![Structure Chart](./images/structurechart.jpeg)

---
### Flowchart
#### main()
#### sort_characters()
#### view_list()
#### add_character()
#### remove_character()
---
### Pseudocode
#### main()
```
BEGIN main()
    favlist = {}
    exit = False
    WHILE exit is not True
        DISPLAY '[MLP Character Guide!] 1.Search character 2.Sort characters 3.View favourites list 4.Exit'
        INPUT choice
        IF choice is 1 THEN
            DISPLAY 'What character would you like to search?: '
            INPUT name
            search_character(name)
        ELIF choice is 2 THEN
            sort_characters()
        ELIF choice is 3 THEN
            view_list()
        ELIF choice is 4 THEN
            DISPLAY 'Exiting program...'
            exit = True
        ELSE
            DISPLAY 'Invalid input. Reloading Main Menu...'
        ENDIF

END main()
```
#### search_character()
```
BEGIN search_character(name)
    IF name is in API THEN
    ELSE
    ENDIF
END search_character(name)
```
#### sort_characters()
```
BEGIN sort_characters()
    DISPLAY 'What would you like to sort characters by? 1.Sex 2.Type'
    INPUT sort
    IF sort is 1 THEN
        DISPLAY 'Sort by: 1. Female 2. Male'
        INPUT sex
        IF sex is 1 THEN
        ELIF sex is 2 THEN
        ELSE
            "Invalid input. Choose either option 1 or 2. Returning to main menu...'
        ENDIF
    ELIF sort is 2 THEN
        DISPLAY 'Sort by: 1. Pegasus 2. Earth Pony 3. Unicorn 4. Other creatures'
        INPUT type
        IF type is 1 or 2 or 3 or 4 THEN
        ELSE
            DISPLAY 'Invalid input. Choose option between 1-4 (1/2/3/4). Returning to main menu...'
    ELSE
        DISPLAY 'Invalid input. Choose option 1 or 2. Returning to main menu...'
    ENDIF
END sort_characters()
```
#### view_list()
```
BEGIN view_list()
    exit = False
    WHILE exit is False
        DISPLAY favlist()
        DISPLAY '1. Add character 2. Remove Character 3. Exit favourites list'
        INPUT choice
        IF choice is 1 THEN
            add_character()
        ELIF choice is 2 THEN
            remove_character()
        ELIF choice is 3 THEN
            DISPLAY 'Exiting favourites list...'
            exit = True
        ELSE 
            DISPLAY 'Invalid input. Choose a number between 1-3 (1/2/3). Reloading favourites list...
        ENDIF


END view_list()
```
#### add_character()
```
BEGIN add_character()
    DISPLAY 'What character would you like to add to favourites? : '
    INPUT character
    IF character is in favlist() THEN
        DISPLAY 'Character already in favourites.'
    ELIF character is in API THEN
        ADD character to favlist()
        DISPLAY 'Character successfully added!'
    ELSE
        DISPLAY 'Invalid input. Character does not exist.'
    ENDIF


END add_character()
```
#### remove_character()
```
BEGIN remove_character()
    DISPLAY 'What character would you like to remove from favourites? : '
    INPUT character
    IF character is in favlist() THEN
        DELETE character from favlist()
        DISPLAY 'Character successfully removed!'
    ELSE
        DISPLAY 'Invalid input. Character not found in list.'
    ENDIF
END remove_character()
```

---
### Data Dictionary
| Variable | Data Type | Format for Display | Size in Bytes | Size for Display | Description | Example | Validation |
|-|-|-|-|-|-|-|-|

---
### Gantt Chart
![Gantt Chart](./images/Ganttchart.png)
## Development
## Integration
## Testing and Debugging
### Student Feedback #1 - Yuna Shin
- feedback based on functional and nonfunctional requirements, response time, load testing and the suitability of the requirements.txt and README.md file

### Student Feedback #2 - Isabella Usacheva
- feedback based on functional and nonfunctional requirements, response time, load testing and the suitability of the requirements.txt and README.md file

## Maintenance
Evaluate the role that maintenance would play in the continued implementation of this software 