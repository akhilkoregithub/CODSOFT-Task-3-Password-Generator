import tkinter as tk
import random
import string

# generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_result.set("Password length must be greater than 0")
            return

        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_result.set(password)
    except ValueError:
        password_result.set("Invalid input. Please enter a valid number.")

# main application window
root = tk.Tk()
root.title("Password Generator")

# x and y coordinates to center the window
window_width = 400 
window_height = 300 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

#window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# grid rows and columns to center widgets
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# password length with a border
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')

length_entry = tk.Entry(root, relief=tk.SOLID, borderwidth=1)
length_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

# Button to generate password 
generate_button = tk.Button(root, text="Generate Password", command=generate_password, width=20, height=2, relief=tk.SOLID, borderwidth=1, bg="blue", fg="white")
generate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=2, sticky='n', ipadx=10)

# display the generated password
password_result = tk.StringVar()
password_label = tk.Label(root, textvariable=password_result)
password_label.grid(row=2, column=0, columnspan=3, padx=10, pady=2, sticky='n')

# Tkinter main loop
root.mainloop()
