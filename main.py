from functions import * # Import all modules/libraries imported in functions.py

# Create a dataframe called log_df with columns "TIMESTAMP", "ACTION" and "USER INPUT"
log_df = pd.DataFrame(columns=["TIMESTAMP", "ACTION", "USER INPUT"]) 

def main():
    while True:
        print("""
 ____________________________________
|  ₊☆. ݁˖ MLP Character Guide˚ ✧‧₊⁀➷  |
|------------------------------------|
| 1.Search for character             | 
| 2.Filter all characters            |
| 3.View favourites list             |
| 4.View user interactions log       |
| 5.Exit                             |
|                                    |
| (If you have a problem with the    |
| program or need help at any point, |
| press 'h'!)                        |
 ____________________________________""")
        time.sleep(1)
        user_input = input("""
Choose an option (1/2/3/4/5): """).strip()
        time.sleep(1)
        if user_input == '1':
            name = input("""
Enter full name of character to search: """).strip()
            time.sleep(1)
            # Record user interaction in log_df
            record_actions(log_df, "search character", name)
            character = search_character(name) # Call search_character() function and store in character
            if character:
                print("")
                for key, value in character.items(): 
                    if key != "Image": # Check key in dictionary is not "Image" before displaying to user
                        print(f"\033[1m{key}\033[0m: {value}")
                    else: 
                        display_image(character["Image"]) # Call display_image() function to visualise image in terminal
            elif character.lowercase() == 'h':
                pass
        elif user_input == '2':
            filter_characters(log_df) # Call filter_characters() function
        elif user_input == '3':
            view_list(log_df) # Call view_list() function
        elif user_input == '4':
            # Check if log_df is empty
            if log_df.empty:
                print("""
User interactions log is empty. Returning to main menu...""")
            # Display log_df
            else:
                print("")
                print(log_df.to_string(index=False)) # Display log_df as a string to users
        elif user_input == '5':
            print("""
 ________________________________ 
| Exiting MLP Character Guide... |
 ________________________________""")
            break
        elif user_input.lowercase() == 'h':
            pass
        else:
            print("""
Invalid input. Enter a number between 1-4 (1/2/3/4). Please try again""") # Display user input error message
        time.sleep(2)
        
if __name__ == "__main__":
    main()


