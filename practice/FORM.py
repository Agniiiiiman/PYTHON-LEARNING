import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    policy_number = policynumber_entry.get()
    branch_code = branchcode_entry.get()
    branch_name = branchname_entry.get()
    

    if name and email and phone and address and policy_number and branch_code and branch_name:
        messagebox.showinfo("Form Submitted", 
                            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\nPolicy Number: {policy_number}\nBranch Code: {branch_code}\nBranch Name: {branch_name}")
    else:
        messagebox.showwarning("Missing Info", "Please fill all the fields")

# Create the main window
root = tk.Tk()
root.title("Customer Information Form")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Header
tk.Label(root, text="Customer Information Form", font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

# Labels and Entry Fields
tk.Label(root, text="Name:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
phone_entry = tk.Entry(root, width=40)
phone_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
address_entry = tk.Entry(root, width=40)
address_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Policy Number:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
policynumber_entry = tk.Entry(root, width=40)
policynumber_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Branch Code:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
branchcode_entry = tk.Entry(root, width=40)
branchcode_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Branch Name:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=7, column=0, sticky="e", padx=10, pady=5)
branchname_entry = tk.Entry(root, width=40)
branchname_entry.grid(row=7, column=1, padx=10, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=15, command=submit_form)
submit_btn.grid(row=8, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
