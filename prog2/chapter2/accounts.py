#let's create some initial accounts just for fun
bank=[['Ahmed',1000],['Khaoula',2500],['Said',450]]

# here go the functions
def create_account(name:str,amount:int) -> int:
    if amount<=0:
        raise ValueError("Amount should be > 0")
    bank.append([name,amount])
    return len(bank)-1

def deposit(num:int,amount:int):
    if amount<=0:
        raise ValueError("Amount should be > 0")
    bank[num][1]+=amount

def debit(num:int,amount:int):
    if amount<=0:
        raise ValueError("Amount should be > 0")
    if bank[num][1]<amount:
        raise ValueError("Not enough money")
    else:
        bank[num][1]-=amount

def transfer(num1:int,num2:int,amount:int):
    if amount<=0:
        raise ValueError("Amount should be > 0")
    if num1==num2:
        raise ValueError("Accounts should be different")
    bank[num1][1]-=amount
    bank[num2][1]+=amount

def list_accounts():
    print(f"+ {'-'*20} + {'-'*10} +")
    print(f"| {'Name':<20} | {'Amount':^10} |")
    print(f"+ {'-'*20} + {'-'*10} +")
    for n,a in bank:
        print(f"| {n:<20} | {a:^10} |")
    print(f"+ {'-'*20} + {'-'*10} +")
    input("Press Enter to continue")

if __name__=="__main__":
    print("Developed by the dev team")
