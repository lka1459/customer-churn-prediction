import tkinter as tk
from tkinter import messagebox

def show_message():
    # Retrieve text entered by the user
    user_text = entry.get()
    messagebox.showinfo("Greeting", f"Hello, {user_text}!")

# 1. Initialize the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("400x200")

# 2. Add text instruction (Label)
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# 3. Add an input area (Entry)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# 4. Add an action button (Button)
button = tk.Button(root, text="Submit", command=show_message, bg="lightblue")
button.pack(pady=15)

# 5. Execute the app window loop
root.mainloop()