from tkinter import*

def click_button():
    user_text = entry.get()
    label.config(text="Hello,"+user_text+" ")

root = Tk()
root.title(" Python GUI application")
root.geometry("300x150")

entry = Entry(root)
entry.pack(pady=10)

button = Button(root, text="Click Me", command=click_button,bg="#00D0FF")
button.pack(pady=5)

label = Label(root, text="(Your greeting will appear here)")
label.pack(pady=10)

root.mainloop()
