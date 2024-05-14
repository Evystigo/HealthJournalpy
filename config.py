import json
import os
from utils.classes import User

def load_config(file_path="config.json"):
    """
    Load and return the application configuration from a JSON file.
    :param file_path: Path to the JSON configuration file, default is 'config.json'.
    :return: A dictionary with the configuration settings.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    return {}

def load_user(filename='user.json'):
    """
    Load and return the user data from a JSON file.
    :param filename: Path to the JSON user data file, default is 'user.json'.
    :return: A User object with the user data.
    """
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as file:
            try:
                user_data = json.load(file)
                return User.from_dict(user_data)
            except json.JSONDecodeError:
                print("Error decoding JSON from user.json")
                return None
    return None

def save_user(user, filename='user.json'):
    """
    Save the user data to a JSON file.
    :param user: The User object to save.
    :param filename: Path to the JSON user data file, default is 'user.json'.
    """
    with open(filename, 'w') as file:
        json.dump(user.to_dict(), file, indent=4)
    print("User data saved.")
