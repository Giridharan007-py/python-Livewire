from tkinter import *
from tkinter import messagebox
from datetime import datetime

def main():
    r = Tk()
    r.geometry("500x700")
    r.title("Customer Application")
    r.configure(bg="#4d7095")
    var1 = IntVar()

    Label(r, text="AXIS BANK", font=("Arial", 20, "bold"), bg="#339FB8", fg="white").place(x=150, y=7, width=180)
    footer_frame = Frame(r, bg="#3399ff", height=50)
    footer_frame.pack(side='bottom', fill='x')
    Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=15)

    form_frame = Frame(r, bg="#ffffff", highlightbackground="#ffffff", highlightthickness=1)
    form_frame.place(x=30, y=65, width=440, height=540)

    Radiobutton(r, text="Login account", variable=var1, value=1, font=("Arial", 15), bg="#ffffff").place(x=150, y=140)
    Radiobutton(r, text="Create account", variable=var1, value=2, font=("Arial", 15), bg="#ffffff").place(x=150, y=180)

    Label(form_frame, text="Welcome!", font=("Helvetica", 25, "bold"), bg="white", fg="#2c3e50").pack(pady=(0, 20))

    def next1():
        if var1.get() == 1:
            r.destroy()
            login()
        elif var1.get() == 2:
            r.destroy()
            create()
        else:
            messagebox.showwarning("Select Option", "Please select an option.")

    Button(r, text="NEXT >>", bg="#3399ff", command=next1).place(x=200, y=250)
    r.mainloop()

def login():
    log = Tk()
    log.geometry("500x700")
    log.title("Login Form")
    log.configure(bg="#4d7095")

    Label(log, text="LOGIN ACCOUNT", font=("Arial", 20, "bold"), bg="#339FB8", fg="white").place(x=110, y=7, width=280)
    Frame(log, bg="#3399ff", height=50).pack(side='bottom', fill='x')

    form_frame = Frame(log, bg="#ffffff", highlightbackground="#ffffff", highlightthickness=1)
    form_frame.place(x=30, y=65, width=440, height=540)

    Label(log, text="Account number", bg="#ffffff").place(x=50, y=80)
    Label(log, text="PIN number", bg="#ffffff").place(x=50, y=120)
    e1 = Entry(log)
    e1.place(x=170, y=80, width=200)
    e2 = Entry(log, show="*")
    e2.place(x=170, y=120, width=200)

    def check():
        acc_no = e1.get().strip()
        pin = e2.get().strip()
        found = False
        try:
            with open("bank_application_data.txt", "r") as f:
                for line in f:
                    data = line.strip().split("\t")
                    if len(data) >= 4 and data[0] == acc_no and data[3] == pin:
                        found = True
                        log.destroy()
                        menu(acc_no, pin)
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")
            return

        if not found:
            messagebox.showwarning("ERROR", "Invalid Account number or PIN.")

    Button(log, text="LOG IN >>", bg="#3399ff", command=check).place(x=200, y=250)

def create():
    cre = Tk()
    cre.geometry("500x700")
    cre.title("Create Account")
    cre.configure(bg="#4d7095")

    Label(cre, text="CREATE ACCOUNT", font=("Arial", 20, "bold"), bg="#339FB8", fg="white").place(x=110, y=7, width=280)
    Frame(cre, bg="#3399ff", height=50).pack(side='bottom', fill='x')

    form_frame = Frame(cre, bg="#ffffff", highlightbackground="#ffffff", highlightthickness=1)
    form_frame.place(x=30, y=65, width=440, height=540)

    Label(cre, text="Account number", bg="#ffffff").place(x=50, y=80)
    Label(cre, text="Name", bg="#ffffff").place(x=50, y=120)
    Label(cre, text="Balance", bg="#ffffff").place(x=50, y=160)
    Label(cre, text="PIN number", bg="#ffffff").place(x=50, y=200)

    e1 = Entry(cre)
    e1.place(x=170, y=80, width=200)
    e2 = Entry(cre)
    e2.place(x=170, y=120, width=200)
    e3 = Entry(cre)
    e3.place(x=170, y=160, width=200)
    e4 = Entry(cre, show="*")
    e4.place(x=170, y=200, width=200)

    def submit():
        acc_no = e1.get().strip()
        name = e2.get().strip()
        balance = e3.get().strip()
        pin = e4.get().strip()

        if not acc_no or not name or not balance or not pin:
            messagebox.showwarning("Incomplete", "Please fill all fields.")
            return

        if not acc_no.isdigit() or not pin.isdigit():
            messagebox.showerror("Invalid Input", "Account number and PIN must be numeric.")
            return

        try:
            float(balance)
        except ValueError:
            messagebox.showerror("Invalid Input", "Balance must be a number.")
            return

        try:
            with open("bank_application_data.txt", "r") as f:
                for line in f:
                    if acc_no == line.strip().split("\t")[0]:
                        messagebox.showwarning("Duplicate", "Account number already exists.")
                        return
        except FileNotFoundError:
            pass

        with open("bank_application_data.txt", "a") as f:
            f.write(f"{acc_no}\t{name}\t{balance}\t{pin}\n")

        messagebox.showinfo("Success", "Account created successfully!")
        cre.destroy()
        menu(acc_no, pin)

    Button(cre, text="Submit", bg="#3399ff", command=submit).place(x=170, y=250)

def menu(acc_no, pin):
    m = Tk()
    m.geometry("500x700")
    m.title("Bank Customer Service")
    m.configure(bg="#4d7095")
    var2 = IntVar()

    Label(m, text="MENU", font=("Arial", 20, "bold"), bg="#339FB8", fg="white").place(x=150, y=7, width=180)
    Frame(m, bg="#3399ff", height=50).pack(side='bottom', fill='x')
    form_frame = Frame(m, bg="#ffffff", highlightbackground="#ffffff", highlightthickness=1)
    form_frame.place(x=30, y=65, width=440, height=600)

    options = [
        ("View Account", 1),
        ("Deposit", 2),
        ("Withdraw", 3),
        ("Transaction History", 4),
        ("Transfer Money", 5),
        ("Change PIN", 6),
        ("Exit", 7)
    ]

    y_pos = 80
    for text, val in options:
        Radiobutton(m, text=text, variable=var2, value=val, font=("Arial", 14), bg="#ffffff").place(x=150, y=y_pos)
        y_pos += 40

    def next2():
        option = var2.get()
        if option == 1:
            view_account(acc_no, pin)
        elif option == 2:
            transaction_window(acc_no, is_deposit=True)
        elif option == 3:
            transaction_window(acc_no, is_deposit=False)
        elif option == 4:
            show_transaction_history(acc_no)
        elif option == 5:
            transfer_money_window(acc_no)
        elif option == 6:
            change_pin_window(acc_no)
        elif option == 7:
            messagebox.showinfo("Exit", "Thank you for using the bank app.")
            m.destroy()

    Button(m, text="NEXT >>", bg="#3399ff", command=next2).place(x=200, y=470)

def view_account(acc_no, pin):
    try:
        with open("bank_application_data.txt", "r") as f:
            for line in f:
                data = line.strip().split("\t")
                if data[0] == acc_no and data[3] == pin:
                    messagebox.showinfo("Account Info", f"Account Number: {data[0]}\nName: {data[1]}\nBalance: ₹{data[2]}")
                    return
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found.")
    messagebox.showwarning("Not Found", "Account not found or incorrect PIN.")

def transaction_window(acc_no, is_deposit):
    t = Tk()
    t.geometry("300x200")
    t.title("Transaction")

    Label(t, text="Enter amount:").pack(pady=10)
    amt_entry = Entry(t)
    amt_entry.pack()

    def process():
        try:
            amt = float(amt_entry.get())
            if amt <= 0:
                raise ValueError
            update_balance(acc_no, amt, is_deposit)
            t.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid positive amount.")

    Button(t, text="Submit", command=process).pack(pady=20)

def update_balance(acc_no, amount, is_deposit):
    lines = []
    found = False

    try:
        with open("bank_application_data.txt", "r") as f:
            for line in f:
                data = line.strip().split("\t")
                if data[0] == acc_no:
                    balance = float(data[2])
                    if is_deposit:
                        balance += amount
                    elif balance >= amount:
                        balance -= amount
                    else:
                        messagebox.showwarning("ERROR", "Insufficient balance.")
                        return
                    data[2] = str(balance)
                    found = True
                lines.append("\t".join(data))
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found.")
        return

    if found:
        with open("bank_application_data.txt", "w") as f:
            for line in lines:
                f.write(line + "\n")
        txn_type = "Deposit" if is_deposit else "Withdraw"
        log_transaction(acc_no, txn_type, amount)
    else:
        messagebox.showwarning("ERROR", "Account not found.")

def log_transaction(acc_no, txn_type, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("transaction_history.txt", "a") as f:
        f.write(f"{acc_no}\t{txn_type}\t{amount}\t{timestamp}\n")

def show_transaction_history(acc_no):
    history = []
    try:
        with open("transaction_history.txt", "r") as f:
            for line in f:
                data = line.strip().split("\t")
                if data[0] == acc_no:
                    history.append(f"{data[3]} - {data[1]} ₹{data[2]}")
    except FileNotFoundError:
        messagebox.showinfo("No History", "No transaction history found.")
        return

    if not history:
        messagebox.showinfo("No History", "No transaction history available for this account.")
    else:
        hist = Tk()
        hist.title("Transaction History")
        hist.geometry("400x300")

        text_area = Text(hist, wrap="word")
        text_area.pack(expand=True, fill="both")

        scrollbar = Scrollbar(text_area)
        scrollbar.pack(side="right", fill="y")
        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_area.yview)

        for entry in history:
            text_area.insert(END, entry + "\n")
        text_area.config(state="disabled")

def transfer_money_window(acc_no):
    w = Tk()
    w.geometry("350x220")
    w.title("Transfer Money")

    Label(w, text="To Account Number:").pack()
    to_entry = Entry(w)
    to_entry.pack()

    Label(w, text="Amount:").pack()
    amt_entry = Entry(w)
    amt_entry.pack()

    def transfer():
        to_acc = to_entry.get().strip()
        try:
            amt = float(amt_entry.get())
            if amt <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid amount.")
            return

        if to_acc == acc_no:
            messagebox.showwarning("Invalid", "Cannot transfer to the same account.")
            return

        recipient_found = False
        try:
            with open("bank_application_data.txt", "r") as f:
                for line in f:
                    if line.startswith(to_acc + "\t"):
                        recipient_found = True
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "Bank data file not found.")
            return
        w.destroy()
        if not recipient_found:
            messagebox.showerror("Invalid", "Recipient account does not exist.")
            return

        update_balance(acc_no, amt, is_deposit=False)
        update_balance(to_acc, amt, is_deposit=True)
        log_transaction(acc_no, "Transfer Out", amt)
        log_transaction(to_acc, "Transfer In", amt)
        messagebox.showinfo("Success", "Transaction successful.")
        

    Button(w, text="Submit", command=lambda:transfer()).pack(pady=10)

def change_pin_window(acc_no):
    cp = Tk()
    cp.geometry("300x180")
    cp.title("Change PIN")

    Label(cp, text="New PIN:").pack()
    new_pin = Entry(cp, show="*")
    new_pin.pack()

    def change():
        pin = new_pin.get().strip()
        if not pin.isdigit():
            messagebox.showerror("Invalid", "PIN must be numeric.")
            return

        lines = []
        with open("bank_application_data.txt", "r") as f:
            for line in f:
                data = line.strip().split("\t")
                if data[0] == acc_no:
                    data[3] = pin
                lines.append("\t".join(data))

        with open("bank_application_data.txt", "w") as f:
            for line in lines:
                f.write(line + "\n")
        messagebox.showinfo("Success", "PIN changed successfully.")
        cp.destroy()

    Button(cp, text="Change", command=change).pack(pady=10)

main()