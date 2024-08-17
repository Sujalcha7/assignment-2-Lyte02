import json

USER_DATA_FILE = 'user_data.json'
with open(USER_DATA_FILE, 'r') as file:
    user_data = json.load(file)


def save_user_data():
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

def sign_up():
    username = input("Enter Username: ")
    if username in user_data:
        print("Username already exists! Try a different username.")
        return

    password = input("Enter Password: ")
    mobile_number = input("Enter Mobile Number: ")

    user_data[username] = {
        'password': password,
        'mobile_number': mobile_number
    }

    save_user_data()
    print("Sign up successful!")

def sign_in():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device! Your mobile number is {user_data[username]['mobile_number']}.")
    else:
        print("Incorrect credentials!")

def main():
    print("1. Sign Up")
    print("2. Sign In")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
