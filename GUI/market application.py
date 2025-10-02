
'''
import tkinter as tk
from tkinter import messagebox
import datetime

# Initialize global bill list
bill_items = []

def add_item():
    item = entry_item.get()
    qty = entry_qty.get()
    price = entry_price.get()

    if item and qty.isdigit() and price.replace('.', '', 1).isdigit():
        total = int(qty) * float(price)
        bill_items.append((item, qty, price, total))
        bill_display.insert(tk.END, f"{item} x {qty} @ {price} = {total:.2f}\n")
        entry_item.delete(0, tk.END)
        entry_qty.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    else:
        messagebox.showerror("Invalid Input", "Please enter valid item, quantity, and price.")

def generate_bill():
    customer = entry_customer.get().strip()
    if not customer:
        messagebox.showerror("Missing Info", "Enter customer name.")
        return
    if not bill_items:
        messagebox.showerror("Empty Bill", "Add at least one item.")
        return

    total_amount = sum(item[3] for item in bill_items)
    now = datetime.datetime.now()
    bill_text = f"Bill for: {customer}\nDate: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    bill_text += "-"*40 + "\n"
    for item, qty, price, total in bill_items:
        bill_text += f"{item} x {qty} @ {price} = {total:.2f}\n"
    bill_text += "-"*40 + f"\nTotal: {total_amount:.2f}\n"

    filename = f"bill_{customer.replace(' ', '_').lower()}.txt"
    with open(filename, 'w') as f:
        f.write(bill_text)

    bill_display.insert(tk.END, f"\n--- Bill saved to {filename} ---\n")
    messagebox.showinfo("Success", f"Bill saved as {filename}")

# GUI Setup
root = tk.Tk()
root.title("Billing System")

# Customer name
tk.Label(root, text="Customer Name:").grid(row=0, column=0, sticky="e")
entry_customer = tk.Entry(root, width=30)
entry_customer.grid(row=0, column=1, columnspan=2)

# Item input
tk.Label(root, text="Item:").grid(row=1, column=0)
entry_item = tk.Entry(root)
entry_item.grid(row=1, column=1)

tk.Label(root, text="Quantity:").grid(row=2, column=0)
entry_qty = tk.Entry(root)
entry_qty.grid(row=2, column=1)

tk.Label(root, text="Price:").grid(row=3, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=3, column=1)

tk.Button(root, text="Add Item", command=add_item).grid(row=4, column=1, pady=5)

# Bill display area
bill_display = tk.Text(root, height=15, width=50)
bill_display.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Generate Bill
tk.Button(root, text="Generate Bill", command=generate_bill, bg="green", fg="white").grid(row=6, column=1, pady=10)

root.mainloop()
'''



import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import csv
import os

try:
    from fpdf import FPDF
    HAS_FPDF = True
except ImportError:
    HAS_FPDF = False

bill_items = []

def add_item():
    item = combo_item.get()
    qty = entry_qty.get()
    price = entry_price.get()

    if item and qty.replace('.', '', 1).isdigit() and price.replace('.', '', 1).isdigit():
        total = float(qty) * float(price)
        bill_items.append((item, qty, price, total))
        bill_display.insert(tk.END, f"{item} x {qty} @ {price} = {total:.2f}\n")
        combo_item.set("")
        entry_qty.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        bill_display.see(tk.END)
    else:
        messagebox.showerror("Invalid Input", "Enter valid item, quantity, and price.")

def delete_last_item():
    if bill_items:
        bill_items.pop()
        bill_display.delete("1.0", tk.END)
        for item, qty, price, total in bill_items:
            bill_display.insert(tk.END, f"{item} x {qty} @ {price} = {total:.2f}\n")
    else:
        messagebox.showinfo("Info", "No items to delete.")

def reset_all():
    entry_customer.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    combo_item.set("")
    entry_qty.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_discount.delete(0, tk.END)
    entry_tax.delete(0, tk.END)
    bill_display.delete("1.0", tk.END)
    bill_items.clear()

def generate_bill():
    customer = entry_customer.get().strip()
    phone = entry_phone.get().strip()
    address = entry_address.get().strip()
    discount = entry_discount.get()
    tax = entry_tax.get()

    if not customer:
        messagebox.showerror("Missing Info", "Enter customer name.")
        return
    if not bill_items:
        messagebox.showerror("Empty Bill", "Add at least one item.")
        return

    discount = float(discount) if discount.replace('.', '', 1).isdigit() else 0
    tax = float(tax) if tax.replace('.', '', 1).isdigit() else 0

    subtotal = sum(float(item[3]) for item in bill_items)
    discount_amt = subtotal * (discount / 100)
    tax_amt = (subtotal - discount_amt) * (tax / 100)
    grand_total = subtotal - discount_amt + tax_amt

    now = datetime.datetime.now()
    filename = f"bill_{customer.replace(' ', '_').lower()}_{now.strftime('%Y%m%d_%H%M%S')}"

    bill_text = f"Customer: {customer}\nPhone: {phone}\nAddress: {address}\nDate: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    bill_text += "-"*40 + "\n"
    for item, qty, price, total in bill_items:
        bill_text += f"{item} x {qty} @ {price} = {total:.2f}\n"
    bill_text += "-"*40
    bill_text += f"\nSubtotal: {subtotal:.2f}\nDiscount ({discount}%): -{discount_amt:.2f}"
    bill_text += f"\nTax ({tax}%): +{tax_amt:.2f}\nTotal: {grand_total:.2f}\n"

    txt_filename = filename + ".txt"
    with open(txt_filename, 'w') as f:
        f.write(bill_text)

    # Save to CSV log
    with open("bills.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([now.strftime('%Y-%m-%d %H:%M:%S'), customer, phone, address, subtotal, discount, tax, grand_total])

    # Optional PDF
    if HAS_FPDF:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in bill_text.split('\n'):
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output(filename + ".pdf")

    bill_display.insert(tk.END, f"\n--- Bill saved as {txt_filename} ---\n")
    messagebox.showinfo("Saved", f"Bill saved as:\n{txt_filename}\n(And PDF if FPDF is installed)")

def print_bill():
    try:
        os.startfile(txt_filename, "print")
    except Exception as e:
        messagebox.showerror("Print Error", str(e))

# GUI
root = tk.Tk()
root.title("Advanced Billing System")

tk.Label(root, text="Customer Name:").grid(row=0, column=0, sticky="e")
entry_customer = tk.Entry(root, width=30)
entry_customer.grid(row=0, column=1, columnspan=2)

tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="e")
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Label(root, text="Address:").grid(row=1, column=2, sticky="e")
entry_address = tk.Entry(root)
entry_address.grid(row=1, column=3)

# Items
tk.Label(root, text="Item:").grid(row=2, column=0)
common_items = ["Apple", "Banana", "Milk", "Rice", "Bread"]
combo_item = ttk.Combobox(root, values=common_items)
combo_item.grid(row=2, column=1)

tk.Label(root, text="Quantity:").grid(row=2, column=2)
entry_qty = tk.Entry(root)
entry_qty.grid(row=2, column=3)

tk.Label(root, text="Price:").grid(row=2, column=4)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=5)

tk.Button(root, text="Add Item", command=add_item).grid(row=3, column=1, pady=5)
tk.Button(root, text="Delete Last", command=delete_last_item).grid(row=3, column=2)
tk.Button(root, text="Reset", command=reset_all).grid(row=3, column=3)

# Discounts and Tax
tk.Label(root, text="Discount (%)").grid(row=4, column=0)
entry_discount = tk.Entry(root)
entry_discount.grid(row=4, column=1)

tk.Label(root, text="Tax (%)").grid(row=4, column=2)
entry_tax = tk.Entry(root)
entry_tax.grid(row=4, column=3)

# Display
bill_display = tk.Text(root, height=20, width=80)
bill_display.grid(row=5, column=0, columnspan=6, padx=10, pady=10)

tk.Button(root, text="Generate Bill", command=generate_bill, bg="green", fg="white").grid(row=6, column=1, pady=10)
tk.Button(root, text="Print", command=print_bill, bg="blue", fg="white").grid(row=6, column=2)

root.mainloop()






