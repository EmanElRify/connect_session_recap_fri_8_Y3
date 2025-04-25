import time


account = {
    'name': "",
    'email': "",
    'balance': 0
}


def create_account():
    name = input("Enter your name: ")
    while not (name.isalpha()):
        name = input("Please enter a valid name: ")
    email = input("Enter your email:")
    while "@" not in email:
        email = input("Please enter a valid email: ")
    account = {"name": name, "email": email, "balance": 0}
    return account


def print_pause(msg):
    print(msg)
    time.sleep(1)


def welcom_msg(bank_name):
    #this function is to welcome the user
    print_pause(f"Welcom to {bank_name}!")
    print_pause(f"Please Enter an option\n 1. Create account  2.Exit")


def deposit(balance):
    amount = input("Please enter the amount of money you want to deposit:  ")
    while not (amount.isdigit()):
        amount = input(
            "Please enter a valid  amount of money you want to deposit:  ")

    return float(amount)+balance


def withdraw(balance):
    amount = input("Please enter the amount of money you want to withdraw:  ")
    while not (amount.isdigit()):
        amount = input(
            "Please enter a valid  amount of money you want to withdraw:  ")
    return balance - float(amount)


def view_account_details(account):
    print_pause(f"The user name is {account["name"]}")
    print_pause(f"The user email is {account["email"]}")
    print_pause(f"The user balance is {account["balance"]}")
