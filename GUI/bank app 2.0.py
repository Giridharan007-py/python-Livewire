from tkinter import *
from tkinter import messagebox
from datetime import datetime


def main():
    r = Tk()
    r.geometry("500x700")
    r.title("Customer Application")
    r.configure(bg="#eaf6f6")  # soft light blue background
    var1 = IntVar()

    # Header
    Label(r, text="AXIS BANK", font=("Arial", 24, "bold"), bg="#006d77", fg="white").place(x=0, y=0, width=500, height=60)

    # Main Form Frame
    form_frame = Frame(r, bg="white", bd=2, relief="flat")
    form_frame.place(x=40, y=90, width=420, height=500)

    Label(form_frame, text="Welcome!", font=("Arial", 18, "bold"), bg="white", fg="#006d77").pack(pady=20)

    Label(form_frame, text="Please choose an option below:", font=("Arial", 12), bg="white", fg="#555").pack(pady=10)

    Radiobutton(form_frame, text="Login to your account", variable=var1, value=1,
                font=("Arial", 14), bg="white", fg="#333", selectcolor="#83c5be").pack(pady=10)

    Radiobutton(form_frame, text="Create a new account", variable=var1, value=2,
                font=("Arial", 14), bg="white", fg="#333", selectcolor="#83c5be").pack(pady=10)

    def next1():
        if var1.get() == 1:
            r.destroy()
            login()
        elif var1.get() == 2:
            r.destroy()
            create()

    Button(form_frame, text="NEXT →", font=("Arial", 12, "bold"), bg="#006d77", fg="white",
           activebackground="#005f6b", relief="flat", command=next1).pack(pady=40, ipadx=10, ipady=5)

    # Footer
    footer_frame = Frame(r, bg="#006d77", height=40)
    footer_frame.pack(side='bottom', fill='x')
    Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#006d77", fg="white", font=("Arial", 10)).place(relx=0.5, rely=0.5, anchor='center')

    r.mainloop()


def login():
    log = Tk()
    log.geometry("500x700")
    log.title("Login Form")
    log.configure(bg="#eaf6f6")  # Soft background

    # Header
    Label(log, text="LOGIN ACCOUNT", font=("Arial", 24, "bold"), bg="#006d77", fg="white").place(x=0, y=0, width=500, height=60)

    # Main Form Frame
    form_frame = Frame(log, bg="white", bd=2, relief="flat")
    form_frame.place(x=40, y=90, width=420, height=500)

    Label(form_frame, text="Welcome Back!", font=("Arial", 18, "bold"), bg="white", fg="#006d77").pack(pady=30)

    # Account Number
    Label(form_frame, text="Account Number", font=("Arial", 12), bg="white", fg="#555").pack(pady=(10, 5))
    e1 = Entry(form_frame, font=("Arial", 12), bd=1, relief="solid")
    e1.pack(ipady=5, ipadx=5, padx=30)

    # PIN Number
    Label(form_frame, text="PIN Number", font=("Arial", 12), bg="white", fg="#555").pack(pady=(20, 5))
    e2 = Entry(form_frame, font=("Arial", 12), show="*", bd=1, relief="solid")
    e2.pack(ipady=5, ipadx=5, padx=30)

    # Check login credentials
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

    # Login Button
    Button(form_frame, text="LOG IN →", font=("Arial", 12, "bold"), bg="#006d77", fg="white",
           activebackground="#005f6b", relief="flat", command=check).pack(pady=40, ipadx=10, ipady=5)

    # Footer
    footer = Frame(log, bg="#006d77", height=40)
    footer.pack(side='bottom', fill='x')
    Label(footer, text="© 2025 MyApp. All rights reserved.", bg="#006d77", fg="white", font=("Arial", 10)).place(relx=0.5, rely=0.5, anchor='center')


def create():
    cre = Tk()
    cre.geometry("500x700")
    cre.title("Create Account")
    cre.configure(bg="#eaf6f6")  # Soft modern background

    # Header
    Label(cre, text="CREATE ACCOUNT", font=("Arial", 24, "bold"), bg="#006d77", fg="white").place(x=0, y=0, width=500, height=60)

    # Form container
    form_frame = Frame(cre, bg="white", bd=2, relief="flat")
    form_frame.place(x=40, y=90, width=420, height=500)

    Label(form_frame, text="Open a new account", font=("Arial", 18, "bold"), bg="white", fg="#006d77").pack(pady=20)

    # Field helper
    def create_field(label_text, show=''):
        Label(form_frame, text=label_text, bg="white", fg="#555", font=("Arial", 12)).pack(pady=(10, 5))
        entry = Entry(form_frame, font=("Arial", 12), bd=1, relief="solid", show=show)
        entry.pack(ipady=5, ipadx=5, padx=30)
        return entry

    e1 = create_field("Account Number")
    e2 = create_field("Name")
    e3 = create_field("Balance")
    e4 = create_field("PIN Number", show="*")

    # Submit logic
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

    # Submit button
    Button(form_frame, text="Submit", font=("Arial", 12, "bold"), bg="#006d77", fg="white",
           activebackground="#005f6b", relief="flat", command=submit).pack(pady=40, ipadx=10, ipady=5)

    # Footer
    footer = Frame(cre, bg="#006d77", height=40)
    footer.pack(side='bottom', fill='x')
    Label(footer, text="© 2025 MyApp. All rights reserved.", bg="#006d77", fg="white", font=("Arial", 10)).place(relx=0.5, rely=0.5, anchor='center')


def menu(acc_no, pin):
    m = Tk()
    m.geometry("500x700")
    m.title("Bank Customer Service")
    m.configure(bg="#eaf6f6")  # Soft background

    var2 = IntVar()

    # Header
    Label(m, text="MENU", font=("Arial", 24, "bold"), bg="#006d77", fg="white").place(x=0, y=0, width=500, height=60)

    # Form Frame
    form_frame = Frame(m, bg="white", bd=2, relief="flat")
    form_frame.place(x=40, y=90, width=420, height=540)

    Label(form_frame, text="Please select an option", font=("Arial", 16, "bold"), bg="white", fg="#006d77").pack(pady=20)

    # Menu options
    options = [
        ("View Account", 1),
        ("Deposit", 2),
        ("Withdraw", 3),
        ("Transaction History", 4),
        ("Transfer Money", 5),
        ("Change PIN", 6),
        ("Exit", 7)
    ]

    for text, val in options:
        Radiobutton(form_frame, text=text, variable=var2, value=val,
                    font=("Arial", 13), bg="white", fg="#333", anchor="w",
                    padx=20, pady=5, indicatoron=1).pack(fill='x', padx=40)

    # NEXT button
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

    Button(form_frame, text="NEXT →", font=("Arial", 12, "bold"), bg="#006d77", fg="white",
           activebackground="#005f6b", relief="flat", command=next2).pack(pady=30, ipadx=10, ipady=5)

    # Footer
    footer = Frame(m, bg="#006d77", height=40)
    footer.pack(side='bottom', fill='x')
    Label(footer, text="© 2025 MyApp. All rights reserved.", bg="#006d77", fg="white", font=("Arial", 10)).place(relx=0.5, rely=0.5, anchor='center')

    m.mainloop()


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
    t.geometry("400x300")
    t.title("Transaction")
    t.configure(bg="#eaf6f6")  # Soft pastel background

    # Header
    Label(t, text="DEPOSIT" if is_deposit else "WITHDRAW", font=("Arial", 20, "bold"),
          bg="#006d77", fg="white").place(x=0, y=0, width=400, height=60)

    # Form Card
    form_frame = Frame(t, bg="white", bd=2, relief="flat")
    form_frame.place(x=30, y=90, width=340, height=140)

    Label(form_frame, text="Enter Amount", font=("Arial", 14), bg="white", fg="#333").pack(pady=(20, 10))
    amt_entry = Entry(form_frame, font=("Arial", 12), bd=1, relief="solid")
    amt_entry.pack(ipady=5, ipadx=5, padx=20)

    def process():
        try:
            amt = float(amt_entry.get())
            if amt <= 0:
                raise ValueError
            update_balance(acc_no, amt, is_deposit)
            messagebox.showinfo("Success", f"{'Deposited' if is_deposit else 'Withdrawn'} ₹{amt:.2f} successfully.")
            t.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid positive amount.")

    Button(form_frame, text="Submit", font=("Arial", 12, "bold"), bg="#006d77", fg="white",
           activebackground="#005f6b", relief="flat", command=process).pack(pady=10, ipadx=10, ipady=5)

    # Footer
    footer = Frame(t, bg="#006d77", height=30)
    footer.pack(side='bottom', fill='x')
    Label(footer, text="Secure Transaction", bg="#006d77", fg="white", font=("Arial", 9)).place(relx=0.5, rely=0.5, anchor='center')

    t.mainloop()


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
                    history.append(f"{data[3]} - {data[1]} ₹{float(data[2]):.2f}")
    except FileNotFoundError:
        messagebox.showinfo("No History", "No transaction history found.")
        return

    if not history:
        messagebox.showinfo("No History", "No transaction history available for this account.")
    else:
        hist = Tk()
        hist.title("Transaction History")
        hist.geometry("450x300")
        hist.configure(bg="#ecf0f1")

        Label(hist, text="Your Transaction History", font=("Arial", 14, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=10)

        text_area = Text(hist, wrap="word", font=("Arial", 10), bg="white", fg="black")
        text_area.pack(expand=True, fill="both", padx=10, pady=5)

        scrollbar = Scrollbar(text_area)
        scrollbar.pack(side="right", fill="y")
        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_area.yview)

        for entry in history:
            text_area.insert(END, entry + "\n")
        text_area.config(state="disabled")
    hist.mainloop()


def transfer_money_window(acc_no):
    w = Tk()
    w.geometry("400x250")
    w.title("Transfer Money")
    w.configure(bg="#ecf0f1")  # Light background

    Label(w, text="Transfer Money", font=("Arial", 14, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=10)

    frm = Frame(w, bg="#ecf0f1")
    frm.pack(pady=10)

    Label(frm, text="To Account Number:", bg="#ecf0f1", fg="#34495e", font=("Arial", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
    to_entry = Entry(frm, font=("Arial", 10), width=25)
    to_entry.grid(row=0, column=1, padx=5, pady=5)

    Label(frm, text="Amount (₹):", bg="#ecf0f1", fg="#34495e", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    amt_entry = Entry(frm, font=("Arial", 10), width=25)
    amt_entry.grid(row=1, column=1, padx=5, pady=5)

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
        

    Button(w, text="Submit", command=transfer, bg="#2980b9", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=15)


def change_pin_window(acc_no):
    cp = Tk()
    cp.geometry("350x180")
    cp.title("Change PIN")
    cp.configure(bg="#ecf0f1")

    Label(cp, text="Change PIN", font=("Arial", 14, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=10)
    Label(cp, text="New PIN:", font=("Arial", 10), bg="#ecf0f1", fg="#34495e").pack()

    new_pin = Entry(cp, show="*", font=("Arial", 10), width=25)
    new_pin.pack(pady=5)

    def change():
        # (logic unchanged)
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

    Button(cp, text="Change", command=change, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=10)


main()