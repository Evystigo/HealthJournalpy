# __init__.py for the gui package

# Import the necessary Tkinter modules and any CustomTkinter components
#import tkinter as tk
import customtkinter as ctk

# Setting up a common style or configuration for CustomTkinter
ctk.set_appearance_mode("system")  # 'Light' or 'System' are also options
ctk.set_default_color_theme("blue")  # Setting a color theme for the GUI

# Import GUI components
from .main_window import MainWindow
#from .food_log_view import FoodLogView
#from .nutrition_view import NutritionView
'''
# Optionally, you can define global functions or variables that are used across 
# different GUI components
def create_tooltip(widget, text):
    """
    Create a tooltip for a given widget.
    :param widget: The widget to which the tooltip will be attached.
    :param text: Text displayed in the tooltip.
    """
    tooltip = ctk.CTkLabel(widget, text=text, wraplength=200)
    def enter(event):
        tooltip.place(x=widget.winfo_x(), y=widget.winfo_y() - 30)
    def leave(event):
        tooltip.place_forget()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

# Define any other GUI-wide utilities or configurations here
'''
'''
Key Components:
    Tkinter and CustomTkinter Imports: Essential modules and classes are imported
      at the beginning. This can also include a specific configuration that 
      applies to all GUI components, such as appearance mode and color theme.
      
    GUI Components Import: Import specific GUI components like MainWindow,
      FoodLogView, and NutritionView. This allows you to easily manage and access 
      these components from other parts of your application.

    Shared Functions or Resources: Define functions or global variables that
      might be useful across different GUI components, such as a tooltip creation
      function.

Benefits of This Structure:
    Consistency: Centralizing the import and configuration of GUI-related
      elements ensures a consistent look and behavior across the entire application.

    Simplicity: Reduces the complexity of managing imports and configurations
      in every single GUI component file.

    Reusability: Functions like create_tooltip can be reused in multiple components,
      which adheres to the DRY (Don't Repeat Yourself) principle.

'''