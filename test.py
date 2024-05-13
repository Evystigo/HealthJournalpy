import customtkinter as ctk
import tkinter as tk

# Define the User class
class User:
    def __init__(self):
        self.weight = None
        self.height = None
        self.sex = None
        self.age = None

    def update(self, weight, height, sex, age):
        self.weight = weight
        self.height = height
        self.sex = sex
        self.age = age
        print(f"Weight: {self.weight}, Height: {self.height}, Sex: {self.sex}, Age: {self.age}")

# Initialize the main window
root = ctk.CTk()
root.title("Health Journal")
root.geometry("600x500")

# Center the window on the screen
window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int((screen_height - window_height) / 2)
position_right = int((screen_width - window_width) / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Create a User instance
user = User()

# Menu
menu = ctk.CTkOptionMenu(root, values=["Menu"])
menu.grid(row=0, column=0, padx=10, pady=10)

# User information label
user_info_label = ctk.CTkLabel(root, text="User information", font=("Arial", 20))
user_info_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Weight
weight_label = ctk.CTkLabel(root, text="Weight")
weight_label.grid(row=2, column=0, padx=10, pady=5)
weight_entry = ctk.CTkEntry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=5)

# Height
height_label = ctk.CTkLabel(root, text="Height")
height_label.grid(row=3, column=0, padx=10, pady=5)
height_entry = ctk.CTkEntry(root)
height_entry.grid(row=3, column=1, padx=10, pady=5)

# Sex
sex_label = ctk.CTkLabel(root, text="Sex")
sex_label.grid(row=4, column=0, padx=10, pady=5)
sex_var = tk.StringVar(value="Female")
sex_menu = ctk.CTkOptionMenu(root, values=["Male", "Female"], variable=sex_var)
sex_menu.grid(row=4, column=1, padx=10, pady=5)

# Age
age_label = ctk.CTkLabel(root, text="Age")
age_label.grid(row=5, column=0, padx=10, pady=5)
age_entry = ctk.CTkEntry(root)
age_entry.grid(row=5, column=1, padx=10, pady=5)

# Submit button
submit_button = ctk.CTkButton(root, text="Submit All", command=lambda: submit_all())
submit_button.grid(row=6, column=0, columnspan=3, padx=10, pady=20)

# Submit function
def submit_all():
    weight = weight_entry.get()
    height = height_entry.get()
    sex = sex_var.get()
    age = age_entry.get()
    user.update(weight, height, sex, age)

root.mainloop()
