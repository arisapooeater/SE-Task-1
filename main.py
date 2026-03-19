from functions import *

def main():
    log_df = pd.DataFrame(columns=["ACTION", "USER INPUT"])
    while True:
        print("""
 _______________________________
|      MLP Character Guide      |
|-------------------------------|
| 1.Search for character        | 
| 2.Filter all characters       |
| 3.View favourites list        |
| 4.View user interactions log  |
| 5.Exit                        |
 _______________________________""")
        time.sleep(1)
        user_input = input("""
Choose an option (1/2/3/4/5): """).strip()
        time.sleep(1)
        if user_input == '1':
            name = input("""
Enter full name of character to search: """).strip()
            time.sleep(1)
            log_df.loc[len(log_df)] = ["search", name]
            character = search_character(name)
            if character:
                print("")
                for key, value in character.items():
                    print(f"\033[1m{key}\033[0m: {value}")
        elif user_input == '2':
            log_df.loc[len(log_df)] = ["filter", ""]
            filter_characters() 
        elif user_input == '3':
            log_df.loc[len(log_df)] = ["view favourites list", ""]
            view_list() 
        elif user_input == '4':
            if log_df.empty:
                print("""
User interactions log is empty. Returning to main menu...""")
            else:
                print("")
                print(log_df.to_string(index=False))
        elif user_input == '5':
            print("""
 ________________________________ 
| Exiting MLP Character Guide... |
 ________________________________""")
            break
        else:
            print("""
Invalid input. Enter a number between 1-4 (1/2/3/4). Please try again""")
        time.sleep(2)
        
if __name__ == "__main__":
    main()


