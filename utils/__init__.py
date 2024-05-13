# __init__.py for the utils package

# Importing existing utility functions
from .validators import *
from .converters import *

# Importing health calculation and unit conversion functions from formulas.py
from .formulas import *

# Optionally, include any common utility functions or constants that are used across different modules
def log_message(message, level="INFO"):
    """
    Log a message with a given severity level.
    :param message: The message to log.
    :param level: The severity level of the message (e.g., "INFO", "WARNING", "ERROR").
    """
    print(f"[{level}] {message}")

# Define other utility functions or shared resources here if necessary
