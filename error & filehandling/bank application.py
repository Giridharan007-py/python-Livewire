                            # Simple Bank Application using File Handling:

def create_account():
    acc_no=input("Enter account number: ")
    name=input("Enter name: ")
    balance=input("Enter initial balance: ")
    pin=input("Enter your pin:")
    f=open("bank_data.txt", "a")
    f.write("\n"+acc_no+"\t"+name+"\t"+balance+"\t"+pin)
    print("Account created!\n")
    f.close()

def view_account():
    acc_no = input("Enter account number: ")
    found = False
    f=open("bank_data.txt", "r")
    for line in f:
        data = line.strip().split("\t")
        if data[0]==acc_no:
            print("Account Number:",data[0])
            print("Name:",data[1])
            print("Balance:","₹",data[2])
            found = True
            break
    if not found:
        print("Account not found.\n")

def update_balance(acc_no,amount,is_deposit):
    lines = []
    found = False
    f=open("bank_data.txt", "r")
    for line in f:
        data = line.strip().split("\t")
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
        lines.append("\t".join(data))
    if found:
        f=open("bank_data.txt","w")
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
main()














