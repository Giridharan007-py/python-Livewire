
import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    country = country_combo.get()
    address = text_address.get("1.0", tk.END).strip()

    hobbies = []
    if hobby_reading.get():
        hobbies.append("Reading")
    if hobby_sports.get():
        hobbies.append("Sports")
    if hobby_coding.get():
        hobbies.append("Coding")

    if not name or not email or not password or not gender or not country or not address:
        messagebox.showwarning("Incomplete", "Please fill out all fields.")
        return

    info = f"""
    Name: {name}
    Email: {email}
    Password: {'*' * len(password)}
    Gender: {gender}
    Country: {country}
    Address: {address}
    Hobbies: {', '.join(hobbies)}
    """
    messagebox.showinfo("Submitted Data", info.strip())

# Main Window
root = tk.Tk()
root.title("Stylish Registration Form")
root.geometry("500x700")
root.configure(bg="#e6f2ff")  # light blue background

# Header Frame
header_frame = tk.Frame(root, bg="#3399ff", height=70)
header_frame.pack(fill='x')
tk.Label(header_frame, text="User Registration Form", font=("Arial", 18, "bold"), bg="#339FB8", fg="white").place(x=120, y=20)

# Footer Frame
footer_frame = tk.Frame(root, bg="#3399ff", height=50)
footer_frame.pack(side='bottom', fill='x')
tk.Label(footer_frame, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=15)

# Main Form Frame
form_frame = tk.Frame(root, bg="#ffffff", highlightbackground="#cccccc", highlightthickness=1)
form_frame.place(x=30, y=90, width=440, height=540)

# Inside Form Frame
tk.Label(form_frame, text="Name:", bg="#ffffff").place(x=20, y=20)
entry_name = tk.Entry(form_frame, width=40)
entry_name.place(x=150, y=20)

tk.Label(form_frame, text="Email:", bg="#ffffff").place(x=20, y=60)
entry_email = tk.Entry(form_frame, width=40)
entry_email.place(x=150, y=60)

tk.Label(form_frame, text="Password:", bg="#ffffff").place(x=20, y=100)
entry_password = tk.Entry(form_frame, width=40, show="*")
entry_password.place(x=150, y=100)

tk.Label(form_frame, text="Gender:", bg="#ffffff").place(x=20, y=140)
gender_var = tk.IntVar()
tk.Radiobutton(form_frame, text="Male", variable=gender_var, value=1, bg="#ffffff").place(x=150, y=140)
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value=2, bg="#ffffff").place(x=220, y=140)
tk.Radiobutton(form_frame, text="Other", variable=gender_var, value=3, bg="#ffffff").place(x=300, y=140)

tk.Label(form_frame, text="Hobbies:", bg="#ffffff").place(x=20, y=180)
hobby_reading = tk.BooleanVar()
hobby_sports = tk.BooleanVar()
hobby_coding = tk.BooleanVar()
tk.Checkbutton(form_frame, text="Reading", variable=hobby_reading, bg="#ffffff").place(x=150, y=180)
tk.Checkbutton(form_frame, text="Sports", variable=hobby_sports, bg="#ffffff").place(x=240, y=180)
tk.Checkbutton(form_frame, text="Coding", variable=hobby_coding, bg="#ffffff").place(x=330, y=180)

tk.Label(form_frame, text="Country:", bg="#ffffff").place(x=20, y=220)
country_combo = ttk.Combobox(form_frame, values=["India", "USA", "UK", "Canada", "Australia"], state="readonly", width=37)
country_combo.place(x=150, y=220)
country_combo.current(0)

tk.Label(form_frame, text="Address:", bg="#ffffff").place(x=20, y=260)
text_address = tk.Text(form_frame, height=4, width=30)
text_address.place(x=150, y=260)

tk.Button(form_frame, text="Submit", command=submit_form, bg="#3399ff", fg="white", width=15, font=("Arial", 10, "bold")).place(x=150, y=330)

root.mainloop()
