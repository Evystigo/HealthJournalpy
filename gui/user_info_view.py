import customtkinter as ctk
import tkinter as tk
from utils.classes import User
from config import save_user, load_user
from gui.main_window import MainWindow

class UserInfoView:
    def __init__(self):
        self.user = load_user() or User()
        print(self.user)
        self.root = ctk.CTk()
        self.root.title("User Information")
        self.root.geometry("600x500")

        # Center the window on the screen
        window_width = 600
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int((screen_height - window_height) / 2)
        position_right = int((screen_width - window_width) / 2)
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.create_widgets()
    
    def create_widgets(self):
        # User information label
        user_info_label = ctk.CTkLabel(self.root, text="User information", font=("Arial", 20))
        user_info_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Weight
        weight_label = ctk.CTkLabel(self.root, text="Weight")
        weight_label.grid(row=1, column=0, padx=10, pady=5)
        self.weight_entry = ctk.CTkEntry(self.root)
        #self.weight_entry.insert(0, self.user.weight if self.user.weight else "")
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5)

        # Height
        height_label = ctk.CTkLabel(self.root, text="Height")
        height_label.grid(row=2, column=0, padx=10, pady=5)
        self.height_entry = ctk.CTkEntry(self.root)
        self.height_entry.insert(0, self.user.height if self.user.height else "")
        self.height_entry.grid(row=2, column=1, padx=10, pady=5)

        # Sex
        sex_label = ctk.CTkLabel(self.root, text="Sex")
        sex_label.grid(row=3, column=0, padx=10, pady=5)
        self.sex_var = tk.StringVar(value=self.user.sex if self.user.sex else "Female")
        self.sex_menu = ctk.CTkOptionMenu(self.root, values=["Male", "Female"], variable=self.sex_var)
        self.sex_menu.grid(row=3, column=1, padx=10, pady=5)

        # Age
        age_label = ctk.CTkLabel(self.root, text="Age")
        age_label.grid(row=4, column=0, padx=10, pady=5)
        self.age_entry = ctk.CTkEntry(self.root)
        self.age_entry.insert(0, self.user.age if self.user.age else "")
        self.age_entry.grid(row=4, column=1, padx=10, pady=5)

        # Submit button
        submit_button = ctk.CTkButton(self.root, text="Submit All", command=self.submit_all)
        submit_button.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

    def submit_all(self):
        weight = self.weight_entry.get()
        height = self.height_entry.get()
        sex = self.sex_var.get()
        age = self.age_entry.get()
        self.user.update(weight, height, sex, age)
        save_user(self.user.__dict__)
        self.root.destroy()
        main_window = MainWindow(self.user)
        main_window.run()

    def run(self):
        self.root.mainloop()
