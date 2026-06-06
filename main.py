import pyperclip
import os 

file_name = "password.txt"

def save_password():
    pass

def get_password():
    pass

def main():
    while True:
        print("1. Save password")
        print("2. Get password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            save_password()
         
        elif choice == '2':
            get_password()
        
        elif choice == '3':
            exit()

        else:
            print("Enter a valid option.....")

main()
        