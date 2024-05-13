import json
import os

def load_config(file_path="config.json"):
    """
    Load and return the application configuration from a JSON file.
    :param file_path: Path to the JSON configuration file, default is 'config.json'.
    :return: A dictionary with the configuration settings.
    """
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def load_user(filename='user.json'):
    """
    Load and return the user data from a JSON file.
    :param filename: Path to the JSON user data file, default is 'user.json'.
    :return: A dictionary with the user data.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            user = json.load(file)
        return user
    return None

def save_user(user, filename='user.json'):
    """
    Save the user data to a JSON file.
    :param user: The user data dictionary to save.
    :param filename: Path to the JSON user data file, default is 'user.json'.
    """
    with open(filename, 'w') as file:
        json.dump(user, file, indent=4)

def add_user(user, filename='users.json'):
    """
    Add a new user to the users JSON file.
    :param user: The new user data dictionary to add.
    :param filename: Path to the JSON users data file, default is 'users.json'.
    """
    users = load_user(filename)
    users.append(user)
    save_user(users, filename)

# Example usage
new_user = {
    "id": "003",
    "name": "Charlie",
    "email": "charlie@example.com",
    "preferences": {
        "diet": "omnivore",
        "allergies": ["peanuts"]
    }
}

#add_user(new_user)
