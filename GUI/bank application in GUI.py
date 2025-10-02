                                  # Simple Bank Application using File Handling:
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
    form_frame.place(x=20, y=65, width=440, height=540)

    Radiobutton(r, text="Login account", variable=var1, value=1, font=("Arial", 15), bg="#ffffff").place(x=150, y=100)
    Radiobutton(r, text="Create account", variable=var1, value=2, font=("Arial", 15), bg="#ffffff").place(x=150, y=140)

    def next1():
        if var1.get() == 1:
            r.destroy()
            login()
        elif var1.get() == 2:
            r.destroy()
            create()

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
        acc_no = e1.get()
        pin = e2.get()
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

        if not found:
            messagebox.showwarning("ERROR", "Invalid Account number or PIN.")

    Button(log, text="LOG IN >>", bg="#3399ff",width=10,command=check).place(x=200, y=250)
   # Button(log, text="<< BACK", command=lambda:main(), width=10,bg="#606060", fg="white").place(x=200,y=280)

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
        acc_no = e1.get()
        name = e2.get()
        balance = e3.get()
        pin = e4.get()

        if not acc_no or not name or not balance or not pin:
            messagebox.showwarning("Incomplete", "Please fill all fields.")
            return

        try:
            float(balance)
            int(pin)
        except ValueError:
            messagebox.showerror("Invalid Input", "Balance must be a number and PIN must be numeric.")
            return

        try:
            with open("bank_application_data.txt", "r") as f:
                for line in f:
                    if acc_no in line.split("\t"):
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
    form_frame.place(x=30, y=65, width=440, height=540)

    Radiobutton(m, text="View account", variable=var2, value=1, font=("Arial", 15), bg="#ffffff").place(x=150, y=100)
    Radiobutton(m, text="Deposit", variable=var2, value=2, font=("Arial", 15), bg="#ffffff").place(x=150, y=140)
    Radiobutton(m, text="Withdraw", variable=var2, value=3, font=("Arial", 15), bg="#ffffff").place(x=150, y=180)
    Radiobutton(m, text="Exit", variable=var2, value=4, font=("Arial", 15), bg="#ffffff").place(x=150, y=220)

    def next2():
        option = var2.get()
        if option == 1:     # view account
            view_account(acc_no, pin)
        elif option == 2:   # deposit
            transaction_window(acc_no, is_deposit=True)
        elif option == 3:   # withdraw
            transaction_window(acc_no, is_deposit=False)
        elif option == 4:   # exit
            messagebox.showinfo("Exit", "Thank you for using the bank app.")
            m.destroy()

    Button(m, text="NEXT >>", bg="#3399ff", command=next2).place(x=200, y=280)


def view_account(acc_no, pin):
    found = False
    try:
        with open("bank_application_data.txt", "r") as f:
            for line in f:
                data = line.strip().split("\t")
                if data[0] == acc_no and data[3] == pin:
                    messagebox.showinfo("Account Info", f"Account Number: {data[0]}\nName: {data[1]}\nBalance: ₹{data[2]}")
                    found = True
                    break
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found.")

    if not found:
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
            update_balance(acc_no, amt, is_deposit)
            t.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid amount.")

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
        messagebox.showinfo("Success", "Transaction successful.")
    else:
        messagebox.showwarning("ERROR", "Account not found.")

main()
