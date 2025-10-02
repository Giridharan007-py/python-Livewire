import ttkbootstrap as ttk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    country = country_combo.get()
    address = text_address.get("1.0", "end").strip()

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

# Create a themed app with a Bootstrap theme
app = ttk.Window(themename="flatly")  # Try 'superhero', 'minty', 'darkly', etc.
app.title("Responsive Registration Form")
app.geometry("700x600")
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

# Main Frame
main_frame = ttk.Frame(app, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")
for i in range(10):
    main_frame.rowconfigure(i, weight=1)
main_frame.columnconfigure(1, weight=1)

# Widgets
ttk.Label(main_frame, text="Registration Form", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(main_frame, text="Name:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_name = ttk.Entry(main_frame)
entry_name.grid(row=1, column=1, sticky="ew", pady=5)

ttk.Label(main_frame, text="Email:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_email = ttk.Entry(main_frame)
entry_email.grid(row=2, column=1, sticky="ew", pady=5)

ttk.Label(main_frame, text="Password:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_password = ttk.Entry(main_frame, show="*")
entry_password.grid(row=3, column=1, sticky="ew", pady=5)

ttk.Label(main_frame, text="Gender:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
gender_var = ttk.StringVar()
gender_frame = ttk.Frame(main_frame)
gender_frame.grid(row=4, column=1, sticky="w")
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left", padx=5)
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=5)
ttk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(side="left", padx=5)

ttk.Label(main_frame, text="Hobbies:").grid(row=5, column=0, sticky="e", padx=10, pady=5)
hobby_frame = ttk.Frame(main_frame)
hobby_frame.grid(row=5, column=1, sticky="w")
hobby_reading = ttk.BooleanVar()
hobby_sports = ttk.BooleanVar()
hobby_coding = ttk.BooleanVar()
ttk.Checkbutton(hobby_frame, text="Reading", variable=hobby_reading).pack(side="left", padx=5)
ttk.Checkbutton(hobby_frame, text="Sports", variable=hobby_sports).pack(side="left", padx=5)
ttk.Checkbutton(hobby_frame, text="Coding", variable=hobby_coding).pack(side="left", padx=5)

ttk.Label(main_frame, text="Country:").grid(row=6, column=0, sticky="e", padx=10, pady=5)
country_combo = ttk.Combobox(main_frame, values=["India", "USA", "UK", "Canada", "Australia"], state="readonly")
country_combo.grid(row=6, column=1, sticky="ew", pady=5)
country_combo.current(0)

ttk.Label(main_frame, text="Address:").grid(row=7, column=0, sticky="ne", padx=10, pady=5)
text_address = ttk.Text(main_frame, height=4)
text_address.grid(row=7, column=1, sticky="ew", pady=5)

submit_btn = ttk.Button(main_frame, text="Submit", bootstyle="success", command=submit_form)
submit_btn.grid(row=8, column=0, columnspan=2, pady=20)

app.mainloop()