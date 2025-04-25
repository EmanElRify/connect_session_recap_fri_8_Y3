from utils import welcom_msg, print_pause, create_account, deposit, view_account_details, withdraw
import random
def main():
    banks = ["Banque Misr", "CIB Commercial International Bank", "NBE - National Bank of Egypt", "Banque Du Caire S.A.E."]
    random_bank = random.choice(banks)
    welcom_msg(random_bank)
    option_1 = input()
    while option_1 not in ["1", "2"]:
        option_1=input("Please enter 1 or 2: ")
    if option_1 == "1":
        account = create_account()
        while True:
        
            print_pause("Do you want other operation? \n 1. Deposit\n 2. Withdrawal \n 3. View account details \n 4. Exit")
            operation = input()
            while operation not in ["1", "2", "3", "4"]:
                operation = input ("Please enter 1, 2, 3 or 4")
            if operation == "1":
                account["balance"] = deposit(account["balance"])
            elif operation == "2":
                account["balance"] = withdraw(account["balance"])
            elif operation == "3":
                view_account_details(account)
            else:
                print_pause("Thanks for using our application!\n Have a nice day!")

                break
    else:
        print_pause("Thanks for using our application!\n Have a nice day!")
        
main()