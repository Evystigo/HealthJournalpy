import customtkinter as ctk

class MainWindow:
    def __init__(self, user):
        self.user = user
        self.root = ctk.CTk()
        self.root.title("Health Journal")
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
        # Menu
        menu = ctk.CTkOptionMenu(self.root, values=["Menu"])
        menu.grid(row=0, column=0, padx=10, pady=10)

        # Welcome label
        welcome_label = ctk.CTkLabel(self.root, text=f"Welcome, {self.user.sex}", font=("Arial", 20))
        welcome_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Display User Information
        user_info = f"Weight: {self.user.weight}\nHeight: {self.user.height}\nSex: {self.user.sex}\nAge: {self.user.age}"
        user_info_label = ctk.CTkLabel(self.root, text=user_info, font=("Arial", 16))
        user_info_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def run(self):
        self.root.mainloop()
