# Name: Donna Ng
# Description: A text-based UI of the login page for the music library.

import json


def login():
    option = input(
        "Pick one of the following options:\n1. Log in\n2. Create an account\n")
    if option == '1':
        user_name = input("\nEnter username: ")
        with open('users.json', 'r') as infile:
            user_data = json.load(infile)
        if user_name not in user_data:
            print("Incorrect username! Please try again!\n")
        else:
            password = input("\nEnter password: ")
            if user_data[user_name] == password:
                print(f"\nHello, {user_name}!")
            else:
                print("Incorrect password! Please try again!\n")
    elif option == '2':
        user_name = input("\nEnter a new username: ")
        with open('users.json', 'r') as infile:
            user_data = json.load(infile)
        while user_name in user_data:
            print("\nThis username already exists. Please try again!")
            user_name = input("\nEnter a new username: ")
        password = input("\nEnter a new password: ")
        validate = input("\nConfirm password: ")
        while password != validate:
            print("\nThe passwords do not match! Please try again!")
            password = input("\nEnter a new password: ")
            validate = input("\nConfirm password: ")
        user_data[user_name] = password
        with open('users.json', 'w') as outfile:
            json.dump(user_data, outfile)
        print(f"Your account has been created.\nHello, {user_name}!")
    else:
        print("Incorrect username!\n")


if __name__ == '__main__':
    login()
