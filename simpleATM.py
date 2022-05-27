import os

Balance = 500


def check_Balance():
    return Balance


def show_menu():
    print("****FRASHA'S SANTO'S MENU***\n")
    print("1.Check Balance\n")
    print("2.Deposit\n")
    print("3.Withdraw\n")
    print("4.exit\n")


show_menu()


while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your Bank Balance is KSH ", check_Balance())
    elif choice == 2:
        amount = float(input("Enter amount KSH you want to deposit: "))
        Balance += amount
        print(f"you have deposited {amount} new balance is KSH {Balance} \n")
    elif choice == 3:
        amount = float(input("Enter amount you wish to withdraw: "))

        if amount <= Balance:
            Balance -= amount
            print(f"you have Withdrawn {amount} new balance is KSH {Balance} \n")

        else:
            print("you balance is less than the amount you wish to withdraw")
    elif choice == 4:
        quit()
    else:
        print("invalid choice entered")
        os.system("clear")
