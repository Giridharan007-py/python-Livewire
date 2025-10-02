from tkinter import*
from tkinter import messagebox
from tkinter import ttk
r=Tk()
r.geometry("500x700")
r.title("customer application")
r.configure(bg="#4d7095")
var1=IntVar()

# header_frame

header_frame=Label(r,text="AXIS BANK ",font=("Arial", 20, "bold"),bg="#339FB8",fg="white")
header_frame.place(x=150,y=7,width=180)

# Footer Frame

footer_frame = Frame(r,bg="#3399ff",height=50)
footer_frame.pack(side='bottom',fill='x')
Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=15)

# Main Form Frame'x')

Label(footer_frame, text="© 2025 MyApp")
form_frame = Frame(r, bg="#ffffff",highlightbackground="#ffffff", highlightthickness=1)
form_frame.place(x=30, y=65, width=440, height=540)

old=Radiobutton(r,text="Login account",variable=var1,value=1,font=("Arial", 15),bg="#ffffff").place(x=150,y=100)
new=Radiobutton(r,text="Create account",variable=var1,value=2,font=("Arial", 15),bg="#ffffff").place(x=150,y=140)

def next1():
    if var1.get()==1:
        login(r)
    elif var1.get()==2:
        create(r)


b=Button(r,text="NEXT >>",bg="#3399ff",command=next1)
b.place(x=200,y=250)

def menu(log):
    log.destroy()
    m=Tk()
    m.geometry("500x700")
    m.title("Bank customer service")
    m.configure(bg="#4d7095")
    var2=IntVar()

    # header_frame

    header_frame=Label(m,text="MENU ",font=("Arial", 20, "bold"),bg="#339FB8",fg="white")
    header_frame.place(x=150,y=7,width=180)

    # Footer Frame

    footer_frame = Frame(m,bg="#3399ff",height=50)
    footer_frame.pack(side='bottom',fill='x')
    Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=15)

    # Main Form Frame'x')

    Label(footer_frame, text="© 2025 MyApp")
    form_frame = Frame(m, bg="#ffffff",highlightbackground="#ffffff", highlightthickness=1)
    form_frame.place(x=30, y=65, width=440, height=540)

    
    view=Radiobutton(m,text="View account",variable=var2,value=1,font=("Arial", 15),bg="#ffffff").place(x=150,y=100)
    deposit=Radiobutton(m,text="Deposit",variable=var2,value=2,font=("Arial", 15),bg="#ffffff").place(x=150,y=140)
    withdraw=Radiobutton(m,text="Withdraw",variable=var2,value=3,font=("Arial", 15),bg="#ffffff").place(x=150,y=180)
    exit=Radiobutton(m,text="Exit",variable=var2,value=4,font=("Arial", 15),bg="#ffffff").place(x=150,y=220)

    def next2():
        if var2.get()==1:
            
        elif var2.get()==2:
            
        elif var2.get()==3:
            
        elif var2.get()==4:
        

def login(r):
    r.destroy()
    log=Tk()
    log.geometry("500x700")
    log.title("login form")
    log.configure(bg="#4d7095")
    # header_frame
    header_frame=Label(log,text="LOGIN ACCOUNT ",font=("Arial", 20, "bold"),bg="#339FB8",fg="white")
    header_frame.place(x=110,y=7,width=280)

    # Footer Frame

    footer_frame = Frame(log,bg="#3399ff",height=50)
    footer_frame.pack(side='bottom',fill='x')
    Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=15)

    # Main Form Frame'x')

    Label(footer_frame, text="© 2025 MyApp")
    form_frame = Frame(log, bg="#ffffff",highlightbackground="#ffffff", highlightthickness=1)
    form_frame.place(x=30, y=65, width=440, height=540)

    acc_no=Label(log,text="Account number",bg="#ffffff")
    acc_no.place(x=50,y=80)
    pin=Label(log,text="PIN number",bg="#ffffff")
    pin.place(x=50,y=120)
    e1=Entry(log)
    e1.place(x=170,y=80,width=200)
    e2=Entry(log)
    e2.place(x=170,y=120,width=200)
    
    #b1=Button(log,text="LOG IN >>",bg="#3399ff",command=lambda:check())
    #b1.place(x=200,y=250)
    
    
    def check():
        acc_no =e1.get()
        pin=e2.get()
        found = False
        f=open("bank_application_data.txt", "r")
        for line in f:
            data = line.strip().split("\t")
            if data[0]==acc_no and data[3]==pin:
                found = True
                menu(log)
                break
        if not found:
            messagebox.showwarning("ERROR FOUND", "Please check the Account number and Pin number.")
            return
        b1=Button(log,text="LOG IN >>",command=lambda:check())
        b1.place(x=200,y=250)
        

def create(r):
    r.destroy()
    cre=Tk()
    cre.geometry("500x700")
    cre.title("Application Form")
    cre.configure(bg="#4d7095")
    # header_frame
    header_frame=Label(cre,text="CREATE ACCOUNT ",font=("Arial", 20, "bold"),bg="#339FB8",fg="white")
    header_frame.place(x=110,y=7,width=280)

    # Footer Frame

    footer_frame = Frame(cre,bg="#3399ff",height=50)
    footer_frame.pack(side='bottom',fill='x')
    Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=15)

    # Main Form Frame'x')

    Label(footer_frame, text="© 2025 MyApp")
    form_frame = Frame(cre, bg="#ffffff",highlightbackground="#ffffff", highlightthickness=1)
    form_frame.place(x=30, y=65, width=440, height=540)

    acc_no=Label(cre,text="Account number",bg="#ffffff")
    acc_no.place(x=50,y=80)
    name=Label(cre,text="Name",bg="#ffffff")
    name.place(x=50,y=120)
    bal=Label(cre,text="Balance",bg="#ffffff")
    bal.place(x=50,y=160)
    pin=Label(cre,text="PIN number",bg="#ffffff")
    pin.place(x=50,y=200)
    e1=Entry(cre)
    e1.place(x=170,y=80,width=200)
    e2=Entry(cre)
    e2.place(x=170,y=120,width=200)
    e3=Entry(cre)
    e3.place(x=170,y=160,width=200,)
    e4=Entry(cre,width=40,show="*")
    e4.place(x=170,y=200,width=200)
    
    b=Button(cre,text="Submit",bg="#3399ff",command=lambda:submit())
    b.place(x=170,y=250)

    
def submit(cre,e1,e2):
            acc_no=e1.get()
            name=e2.get()
            balance=e3.get()
            pin=e4.get()

            if not acc_no or not name or not balance or not pin:
                messagebox.showwarning("Incomplete", "Please fill out all fields.")
                return

b=Button(cre,text="Submit",command=lambda:submit())
b.place(x=170,y=250)
f=open("bank_application_data.txt", "a")
f.write("\n"+acc_no+"\t"+name+"\t"+balance+"\t"+pin)
print("Account created!\n")
menu(cre)
f.close()













def create_account():
    acc_no=input("Enter account number: ")
    name=input("Enter name: ")
    balance=input("Enter initial balance: ")
    pin=input("Enter your pin:")
    f=open("bank_application_data.txt", "a")
    f.write("\n"+acc_no+"\t"+name+"\t"+balance+"\t"+pin)
    print("Account created!\n")
    f.close()

def view_account():
    acc_no = input("Enter account number: ")
    found = False
    f=open("bank_applictiondata.txt", "r")
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




r.mainloop()
