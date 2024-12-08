import tkinter as tk
from tkinter import messagebox
import sqlite3


# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Database connection
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Verify user credentials
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Success", f"Welcome {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

    conn.close()


# Function to open registration window
def open_register_window():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    tk.Label(register_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    reg_username = tk.Entry(register_window)
    reg_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(register_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    reg_password = tk.Entry(register_window, show="*")
    reg_password.grid(row=1, column=1, padx=10, pady=10)

    def register():
        new_user = reg_username.get()
        new_pass = reg_password.get()

        if not new_user or not new_pass:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        # Database connection
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()

        # Insert new user
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_user, new_pass))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful!")
            register_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

        conn.close()

    tk.Button(register_window, text="Register", command=register).grid(row=2, column=0, columnspan=2, pady=10)


# Main window setup
root = tk.Tk()
root.title("Login Page")

# UI Elements
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Login", command=login).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Register", command=open_register_window).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
