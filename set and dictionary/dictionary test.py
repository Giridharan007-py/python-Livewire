
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
'''
'''
thisdict = {
  "brand":"Ford",
  "model": "Mustang",
  "year":"1964"
}
print(thisdict[1])
'''

'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset[2])
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024,
  "year": 2025
}
print(thisdict)
print(len(thisdict))
'''
'''
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

'''

''''

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''





















































































































































































'''
def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter name: ")
    balance = input("Enter initial balance: ")
    with open("bank_data.txt", "a") as f:
        f.write(f"{acc_no},{name},{balance}\n")
    print("Account created!\n")



def view_account():
    acc_no = input("Enter account number: ")
    found = False
    with open("bank_data.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == acc_no:
                print(f"Account Number: {data[0]}")
                print(f"Name: {data[1]}")
                print(f"Balance: ₹{data[2]}")
                found = True
                break
    if not found:
        print("Account not found.\n")


def update_balance(acc_no, amount, is_deposit):
    lines = []
    found = False
    with open("bank_data.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == acc_no:
                balance = float(data[2])
                if is_deposit:
                    balance += amount
                elif balance >= amount:
                    balance -= amount
                else:
                    print("Insufficient balance.")
                    return
                data[2] = str(balance)
                found = True
            lines.append(",".join(data))

    if found:
        with open("bank_data.txt", "w") as f:
            for line in lines:
                f.write(line + "\n")
        print("Transaction successful.\n")
    else:
        print("Account not found.\n")


def main():
    while True:
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_account()
        elif choice == "3":
            acc = input("Enter account number: ")
            amt = float(input("Enter amount to deposit: "))
            update_balance(acc, amt, True)
        elif choice == "4":
            acc = input("Enter account number: ")
            amt = float(input("Enter amount to withdraw: "))
            update_balance(acc, amt, False)
        elif choice == "5":
            print("Thank you for using the bank app!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()

'''









