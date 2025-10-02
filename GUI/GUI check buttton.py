  #GUI  CHECKBUTTON
'''
from tkinter import*
r=Tk()
r.geometry("300x300")
c=Checkbutton(r,text="wakeup").pack()
c1=Checkbutton(r,text="GYM class").pack()
c2=Checkbutton(r,text="Breakfast").pack()
c3=Checkbutton(r,text="computer class").pack()
c4=Checkbutton(r,text="lunch").pack()
r.mainloop()
'''


'''
from tkinter import *
from tkinter import messagebox
import tkinter as tk

def login():
    print("Login function called")  # Replace with your login window

def create():
    print("Create function called")  # Replace with your create window

def main():
    root = Tk()
    root.geometry("500x650")
    root.title("Customer Application")
    root.configure(bg="#f0f4f7")

    var1 = IntVar()

    # Title
    title_label = Label(root, text="AXIS BANK", font=("Helvetica", 24, "bold"),
                        bg="#2c3e50", fg="white", pady=15)
    title_label.pack(fill=X)

    # Main Frame
    form_frame = Frame(root, bg="white", padx=30, pady=30)
    form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Subtitle
    Label(form_frame, text="Welcome!", font=("Helvetica", 18, "bold"), bg="white", fg="#2c3e50").pack(pady=(0, 20))

    # Radio Buttons
    Radiobutton(form_frame, text="Login to existing account", variable=var1, value=1,
                font=("Helvetica", 14), bg="white", anchor='w').pack(fill='x', pady=5)
    Radiobutton(form_frame, text="Create a new account", variable=var1, value=2,
                font=("Helvetica", 14), bg="white", anchor='w').pack(fill='x', pady=5)

    # Next Button
    def next1():
        choice = var1.get()
        if choice == 1:
            root.destroy()
            login()
        elif choice == 2:
            root.destroy()
            create()
        else:
            messagebox.showwarning("Selection Required", "Please select an option to proceed.")

    Button(form_frame, text="NEXT →", font=("Helvetica", 12, "bold"),
           bg="#3498db", fg="white", padx=10, pady=5,
           command=next1).pack(pady=30)

    # Footer
    footer = Label(root, text="© 2025 Axis Bank. All rights reserved.",
                   bg="#2c3e50", fg="white", font=("Helvetica", 10))
    footer.pack(side='bottom', fill=X, pady=(10, 0))

    root.mainloop()

main()

'''

'''
import tkinter as tk
from tkinter import messagebox

class AxisBankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AXIS BANK - Customer Portal")
        self.geometry("500x650")
        self.configure(bg="#f0f4f8")
        self.resizable(False, False)
        self.option = tk.IntVar()

        self.show_main_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_main_screen(self):
        self.clear_screen()

        # Header
        tk.Label(self, text="AXIS BANK", font=("Segoe UI", 22, "bold"), bg="#1565C0", fg="white").pack(fill='x', ipady=15)

        frame = tk.Frame(self, bg="white", bd=2, relief="groove")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=420)

        tk.Label(frame, text="Welcome!", font=("Segoe UI", 20, "bold"), bg="white", fg="#2c3e50").pack(pady=20)

        tk.Radiobutton(frame, text="Login to Account", variable=self.option, value=1,
                       font=("Segoe UI", 13), bg="white", fg="#333").pack(pady=10)

        tk.Radiobutton(frame, text="Create New Account", variable=self.option, value=2,
                       font=("Segoe UI", 13), bg="white", fg="#333").pack(pady=10)

        tk.Button(frame, text="NEXT ➜", bg="#1565C0", fg="white", font=("Segoe UI", 12, "bold"),
                  activebackground="#0d47a1", activeforeground="white", padx=10, pady=5,
                  command=self.next_action).pack(pady=40)

        # Footer
        tk.Label(self, text="© 2025 Axis Bank. All rights reserved.", font=("Segoe UI", 9), bg="#f0f4f8", fg="gray").pack(side="bottom", pady=10)

    def next_action(self):
        if self.option.get() == 1:
            self.show_login_screen()
        elif self.option.get() == 2:
            self.show_create_screen()
        else:
            messagebox.showwarning("Choose Option", "Please select an option to continue.")

    def show_login_screen(self):
        self.clear_screen()

        tk.Label(self, text="Login to Your Account", font=("Segoe UI", 20, "bold"), bg="#f0f4f8", fg="#2c3e50").pack(pady=30)

        frame = tk.Frame(self, bg="white")
        frame.pack(pady=10)

        email_var = tk.StringVar()
        pass_var = tk.StringVar()

        self.build_labeled_entry(frame, "Email", email_var, 0)
        self.build_labeled_entry(frame, "Password", pass_var, 1, show="*")

        def login_submit():
            if not email_var.get() or not pass_var.get():
                messagebox.showerror("Missing Fields", "Please fill in all fields.")
            else:
                messagebox.showinfo("Login Success", f"Welcome back, {email_var.get()}!")
                self.show_main_screen()

        tk.Button(self, text="Login", bg="#1565C0", fg="white", font=("Segoe UI", 11, "bold"),
                  command=login_submit, width=20).pack(pady=20)

        tk.Button(self, text="⬅ Back", command=self.show_main_screen, width=10,
                  bg="gray", fg="white").pack()

    def show_create_screen(self):
        self.clear_screen()

        tk.Label(self, text="Create New Account", font=("Segoe UI", 20, "bold"), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)

        frame = tk.Frame(self, bg="white")
        frame.pack(pady=10)

        name_var = tk.StringVar()
        email_var = tk.StringVar()
        phone_var = tk.StringVar()
        pass_var = tk.StringVar()
        confirm_var = tk.StringVar()

        self.build_labeled_entry(frame, "Full Name", name_var, 0)
        self.build_labeled_entry(frame, "Email", email_var, 1)
        self.build_labeled_entry(frame, "Phone", phone_var, 2)
        self.build_labeled_entry(frame, "Password", pass_var, 3, show="*")
        self.build_labeled_entry(frame, "Confirm Password", confirm_var, 4, show="*")

        def create_submit():
            if not all([name_var.get(), email_var.get(), phone_var.get(), pass_var.get(), confirm_var.get()]):
                messagebox.showerror("Missing Fields", "Please fill in all fields.")
                return
            if pass_var.get() != confirm_var.get():
                messagebox.showerror("Password Error", "Passwords do not match.")
                return
            messagebox.showinfo("Success", f"Account created for {name_var.get()}!")
            self.show_main_screen()

        tk.Button(self, text="Create Account", bg="#1565C0", fg="white",
                  font=("Segoe UI", 11, "bold"), command=create_submit, width=20).pack(pady=20)

        tk.Button(self, text="⬅ Back", command=self.show_main_screen, width=10,
                  bg="gray", fg="white").pack()

    def build_labeled_entry(self, parent, label_text, var, row, show=None):
        tk.Label(parent, text=label_text + ":", font=("Segoe UI", 11), bg="white").grid(row=row, column=0, padx=10, pady=10, sticky='e')
        entry = tk.Entry(parent, textvariable=var, font=("Segoe UI", 11), width=30, show=show)
        entry.grid(row=row, column=1, padx=10, pady=10)

# Run the app
if __name__ == "__main__":
    app = AxisBankApp()
    app.mainloop()
'''



from tkinter import *
from tkinter import messagebox
import tkinter as tk


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

    
main()