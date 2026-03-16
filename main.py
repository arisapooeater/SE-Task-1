from functions import *
import time
import os
from datetime import datetime

def main():
    while True:
        print("MLP Character Guide: 1.Search for character 2.Filter all characters 3.View favourites list 4.Exit")
        choice = input("Choose an option (1/2/3/4)")

        if choice == '1':
            name = input("Enter full name of character to search: ")
            print(search_character(name))
        elif choice == '2':
            filter_characters() 
        elif choice == '3':
            view_list() 
        elif choice == '4':
            print("Exiting MLP Character Guide...")
            break
        else:
            print("Invalid option. Please try again")


if __name__ == "__main__":
    main()