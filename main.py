import pyperclip

file_name = "password.txt"

def save_password():
    website = input("Enter website: ")
    password = input("Enter password: ")

    with open(file_name, "a") as f:
        f.write(f"{website}:{password}\n")

    print("Password saved successfully!")

def get_password():
    website = input("Enter website: ")

    try:
        with open(file_name, "r") as f:
            for line in f:
                saved_website, saved_password = line.strip().split(":", 1)

                if saved_website == website:
                    pyperclip.copy(saved_password)
                    print("Password copied to clipboard!")
                    return

        print("Website not found!")

    except FileNotFoundError:
        print("No passwords saved yet!")

def main():
    while True:
        print("\n1. Save Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            save_password()

        elif choice == "2":
            get_password()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Enter a valid option!")

main()