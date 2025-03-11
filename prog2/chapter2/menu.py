from accounts import *
import math




def menu():
    while True:
        print("\n")
        print("C-Create account")
        print("L-List of accounts")
        print("D-Make a deposit")
        print("B-Debit an account")
        print("T-Make a transfer")
        print("Q-Quit")
        cmd=input("Your command: ")
        match cmd.lower():
            case "q":
                break
            case "c":
                name=input("The name: ")
                amount=int(input("Initial amount: "))
                create_account(name,amount)
            case "l":
                list_accounts()
            case "d":
                num=int(input("The account number: "))
                amount=int(input("The amount (>0): "))
                deposit(num,amount)
            case "b":
                num=int(input("The account number: "))
                amount=int(input("The amount (>0): "))
                debit(num,amount)
            case "t":
                num1=int(input("The account number of the sender: "))
                num2=int(input("The account number of the receiver: "))
                amount=int(input("The amount (>0): "))
                transfer(num1,num2,amount)


if __name__=="__main__":
    menu()
