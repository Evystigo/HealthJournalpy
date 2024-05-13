import tkinter as tk
import customtkinter as ctk
'''from gui.main_window import MainWindow
#from apis import init_apis
from config import load_config

def main():
    # Load configuration
    #config = load_config("config.json")

    # Initialize APIs
    #apis = init_apis(config['api_keys'])

    # Setup the main application window
    ctk.set_appearance_mode("system")  # 'Light' or 'System' are also options
    ctk.set_default_color_theme("blue")  # Setting a color theme for the GUI
    root = ctk.CTk()
    app = MainWindow(root)
    app.pack(fill="both", expand=True)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
'''
from gui.user_info_view import UserInfoView

if __name__ == "__main__":
    app = UserInfoView()
    app.run()
