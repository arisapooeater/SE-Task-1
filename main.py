from functions import *
import time
import os

def main():
    while True:
        print("MLP Character Guide: 1.Search for character 2.Sort all characters 3.view favourites list 4.exit")
        choice = input("Choose an option (1/2/3/4)")

        if choice == '1':
            #search_character()
            pass
        elif choice == '2':
            #sort_characters()
            pass
        elif choice == '3':
            #view_list()
            pass
        elif choice == '4':
            print("Exiting MLP Character Guide...")
            break
        else:
            print("Invalid option. Please try again")


#if __name__ == "__main__":
    #main()