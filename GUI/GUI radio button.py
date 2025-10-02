from tkinter import*
from tkinter import messagebox
from tkinter import ttk
r=Tk()
r.geometry("500x700")
r.title("login box")
r.configure(bg="#4d7095")
# header_frame
header_frame=Label(r,text="STUDENT REGISTER FORM",font=("Arial", 20, "bold"),bg="#339FB8",fg="white")
header_frame.place(x=60,y=7,width=380)
# Footer Frame
footer_frame = Frame(r,bg="#3399ff",height=50)
footer_frame.pack(side='bottom',fill='x')
Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=15)
# Main Form Frame'x')
Label(footer_frame, text="© 2025 MyApp")
form_frame = Frame(r, bg="#ffffff",highlightbackground="#ffffff", highlightthickness=1)
form_frame.place(x=30, y=65, width=440, height=540)
name=Label(r,text="Name",bg="#ffffff")
name.place(x=50,y=80)
email=Label(r,text="Email",bg="#ffffff")
email.place(x=50,y=120)
password=Label(r,text="Password",bg="#ffffff")
password.place(x=50,y=160)
phone=Label(r,text="phone number",bg="#ffffff")
phone.place(x=50,y=200)
e1=Entry(r)
e1.place(x=170,y=80,width=200)
e2=Entry(r)
e2.place(x=170,y=120,width=200)
e3=Entry(width=40,show="*")
e3.place(x=170,y=160,width=200,)
e4=Entry(r)
e4.place(x=170,y=200,width=200)
def submit():
    name=e1.get()
    email=e2.get()
    password=e3.get()
    phone=e4.get()

    if not name or not email or not password or not phone:
        messagebox.showwarning("Incomplete", "Please fill out all fields.")
        return

    b=Button(r,text="Submit",command=submit)
    b.place(x=150,y=250)
    f=open("app.txt", "a")
    f.write("\n")
    f.write(f" Name: {name}\n")
    f.write(f"email:{email}\n")
    f.write(f"password: {password}\n")
    f.write(f"Phone Number: {phone}\n")
    print("Account created!\n")
    quiz(r)
    f.close()
b=Button(r,text="Submit",bg="#3399ff",command=submit)
b.place(x=150,y=250)


def quiz(r):
    r.destroy()
    root=Tk()
    root.title("game:QUIZ")
    root.geometry("800x800")
    root.configure(bg="#ffffff")
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    Label(root,text="QUIZ",font=("Arial", 20,"bold")).grid(row=0,column=1)
    
    # QUESTION-1
    ques1=Label(root,text="1.WHAT IS THE INDIA'S NATIONAL ANIMAL ?").grid(row=1,column=0)

    R1=Radiobutton(root,text="TIGER",variable=var1,value=1).grid(row=2,column=0)
    R2=Radiobutton(root,text="LION",variable=var1,value=2).grid(row=2,column=1)
    R3=Radiobutton(root,text="ZEBRA",variable=var1,value=3).grid(row=2,column=2)
    R4=Radiobutton(root,text="MONKEY",variable=var1,value=4).grid(row=2,column=3)

    # QUESTION-2
    ques2=Label(root,text="2.WHAT IS THE INDIA'NATIONAL BIRD ?").grid(row=3,column=0)

    S1=Radiobutton(root,text="PEACOCK",variable=var2,value=1).grid(row=4,column=0)
    S2=Radiobutton(root,text="DOVE",variable=var2,value=2).grid(row=4,column=1)
    S3=Radiobutton(root,text="KINGFISHER",variable=var2,value=3).grid(row=4,column=2)
    S4=Radiobutton(root,text="CROW",variable=var2,value=4).grid(row=4,column=3)

    # QUESTION-3
    ques3 = Label(root, text="3.WHAT IS THE CAPITAL OF FRANCE?").grid(row=5,column=0)

    T1=Radiobutton(root, text="BERLIN", variable=var3, value=1).grid(row=6,column=0)
    T2=Radiobutton(root, text="MADRID", variable=var3, value=2).grid(row=6,column=1)
    T3=Radiobutton(root, text="PARIS", variable=var3, value=3).grid(row=6,column=2)
    T4=Radiobutton(root, text="ROME", variable=var3, value=4).grid(row=6,column=3)
    
    # QUESTION-4
    ques4 = Label(root, text="4.WHICH PLANET IS KNOWN AS THE RED PLANET?").grid(row=7,column=0)

    U1=Radiobutton(root, text="EARTH", variable=var4, value=1).grid(row=8,column=0)
    U2=Radiobutton(root, text="MARS", variable=var4, value=2).grid(row=8,column=1)
    U3=Radiobutton(root, text="JUPITER", variable=var4, value=3).grid(row=8,column=2)
    U4=Radiobutton(root, text="VENUS", variable=var4, value=4).grid(row=8,column=3)

    # QUESTION-5
    ques5 = Label(root, text="5.WHO WROTE THE PLAY 'ROMEO AND JULIET'?").grid(row=9,column=0)

    V1=Radiobutton(root, text="MARK TWAIN", variable=var5, value=1).grid(row=10,column=0)
    V2=Radiobutton(root, text="J.K. ROWLING", variable=var5, value=2).grid(row=10,column=1)
    V3=Radiobutton(root, text="CHARLES DICKENS", variable=var5, value=3).grid(row=10,column=2)
    V4=Radiobutton(root, text="WILLIAM SHAKESPEARE", variable=var5, value=4).grid(row=10,column=3)

    # QUESTION-6
    ques6 = Label(root, text="6.WHAT IS THE LARGEST MAMMAL IN THE WORLD?").grid(row=11,column=0)

    W1=Radiobutton(root, text="AFRICAN ELEPHANT", variable=var6, value=1).grid(row=12,column=0)
    W2=Radiobutton(root, text="BLUE WHALE", variable=var6, value=2).grid(row=12,column=1)
    W3=Radiobutton(root, text="GIRAFFE", variable=var6, value=3).grid(row=12,column=2)
    W4=Radiobutton(root, text="GREAT WHITE SHARK", variable=var6, value=4).grid(row=12,column=3)

    # QUESTION-7
    ques7 = Label(root, text="7.WHO DISCOVERED GRAVITY?").grid(row=13,column=0)

    X1=Radiobutton(root, text="ALBERT EINSTEIN", variable=var7, value=1).grid(row=14,column=0)
    X2=Radiobutton(root, text="ISAAC NEWTON", variable=var7, value=2).grid(row=14,column=1)
    X3=Radiobutton(root, text="GALILEO GALILEI", variable=var7, value=3).grid(row=14,column=2)
    X4=Radiobutton(root, text="STEPHEN HAWKING", variable=var7, value=4).grid(row=14,column=3)

    # Question-8
    ques8 = Label(root, text="8.WHICH IS THE SMALLEST CONTINENT?").grid(row=15,column=0)

    Y1=Radiobutton(root, text="EUROPE", variable=var8, value=1).grid(row=16,column=0)
    Y2=Radiobutton(root, text="ANTARCTICA", variable=var8, value=2).grid(row=16,column=1)
    Y3=Radiobutton(root, text="AUSTRALIA", variable=var8, value=3).grid(row=16,column=2)
    Y4=Radiobutton(root, text="SOUTH AMERICA", variable=var8, value=4).grid(row=16,column=3)

    # Question-9
    ques9 = Label(root, text="9.WHICH IS THE FASTEST LAND ANIMAL?").grid(row=17,column=0)

    Z1=Radiobutton(root, text="LION", variable=var9, value=1).grid(row=18,column=0)
    Z2=Radiobutton(root, text="HORSE", variable=var9, value=2).grid(row=18,column=1)
    Z3=Radiobutton(root, text="CHEETAH", variable=var9, value=3).grid(row=18,column=2)
    Z4=Radiobutton(root, text="LEOPARD", variable=var9, value=4).grid(row=18,column=3)

    # Question-10
    ques10 = Label(root, text="10.WHICH ORGAN PURIFIES OUR BLOOD?").grid(row=19,column=0)

    A1=Radiobutton(root, text="LUNGS", variable=var10, value=1).grid(row=20,column=0)
    A2=Radiobutton(root, text="KIDNEYS", variable=var10, value=2).grid(row=20,column=1)
    A3=Radiobutton(root, text="HEART", variable=var10, value=3).grid(row=20,column=2)
    A4=Radiobutton(root, text="LIVER", variable=var10, value=4).grid(row=20,column=3)
    
    

    def submitfinal():
        marks=0
        if var1.get()==1:
            marks+=1
        if var2.get()==1:
            marks+=1
        if var3.get()==3:
            marks+=1
        if var4.get()==2:
            marks+=1         
        if var5.get()==4:
            marks+=1
        if var6.get()==2:
            marks+=1
        if var7.get()==2:
            marks+=1
        if var8.get()==3:
            marks+=1
        if var9.get()==3:
            marks+=1
        if var10.get()==2:
            marks+=1
        total(root,marks)
    
    
    
    g=Button(root,text="Submit",bg="#3399ff",command=lambda:submitfinal())
    g.grid(row=22,column=1)

    root.mainloop()

def total(root,marks):
    root.destroy
    mark=Tk()
    mark.geometry("300x300")
    mark.configure(bg="#ffffff")
    mark.title("Result")
    Label(mark,text="TOTAL MARKS",font=("Arial", 20,"bold"),bg="#ffffff").grid(row=0,column=0)
    total_marks=Label(mark,text="TOTAL MARK:10",bg="#ffffff",font=("Arial", 15)).grid(row=1,column=0)
    score=Label(mark,text=" YOUR MARK: "+str(marks),bg="#ffffff",font=("Arial", 15)).grid(row=2,column=0)
    percentage=Label(mark,text="PERCENTAGE:"+str(marks/10*100)+"%",bg="#ffffff",font=("Arial", 15)).grid(row=3,column=0)
    
    mark.mainloop()


r.mainloop()
