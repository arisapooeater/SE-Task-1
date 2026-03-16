from functions import *
import time
import os

def main():
    while True:
        print("""
 _________________________
|   MLP Character Guide   |
|-------------------------|
| 1.Search for character  |
| 2.Filter all characters |
| 3.View favourites list  |
| 4.Exit                  |
 _________________________""")
        choice = input("""
Choose an option (1/2/3/4): """).strip()

        if choice == '1':
            name = input("""
Enter full name of character to search: """).strip()
            print(search_character(name))
        elif choice == '2':
            filter_characters() 
        elif choice == '3':
            view_list() 
        elif choice == '4':
            print("""
 ________________________________ 
| Exiting MLP Character Guide... |
 ________________________________""")
            break
        else:
            print("""
Invalid input. Enter a number between 1-4 (1/2/3/4). Please try again""")


if __name__ == "__main__":
    main()


