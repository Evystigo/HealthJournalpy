# commands.py in the gui folder

from utils import calculate_bmi, calculate_bmr, kg_to_lbs, lbs_to_kg

class GUICommands:
    def __init__(self, api_handlers=None, database=None):
        """
        Initialize the commands handler with required APIs and database connections.
        Args:
            api_handlers (dict): Dictionary containing instances of API handlers.
            database: Database connection or handler for data storage and retrieval.
        """
        self.api_handlers = api_handlers
        self.database = database

    '''def add_food_entry(self, food_data):
        """
        Add a new food entry to the database.
        Args:
            food_data (dict): Data about the food item to be added.
        """
        # Assuming a utility function exists to add data to the database
        self.database.add_food_entry(food_data)
        print("Food entry added.")'''

    '''def fetch_nutritional_info(self, barcode):
        """
        Fetch nutritional information for a given food item using its barcode.
        Args:
            barcode (str): Barcode of the food item.
        """
        # Call to an API handler to get the data
        product_info = self.api_handlers['openfoodfacts'].fetch_product(barcode)
        if product_info:
            return product_info
        else:
            print("Failed to fetch product information.")
            return None'''
        
    '''def enter_info():
        try:
            f_info = meal.get()
            print(f_info)
        except:
            print("meal failed")'''

    def calculate_user_bmi(self, weight, height):
        """
        Calculate the BMI for a given weight and height.
        Args:
            weight (float): User's weight in kilograms.
            height (float): User's height in meters.
        Returns:
            float: Calculated BMI.
        """
        return calculate_bmi(weight, height)

    def calculate_user_bmr(self, weight_kg, height_cm, age, sex):
        """
        Calculate the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.
        
        Args:
        weight_kg (float): Weight in kilograms.
        height_cm (float): Height in centimeters.
        age (int): Age in years.
        sex (str): sex 'male' or 'female'.
        
        Returns:
        float: The calculated BMR in calories per day.
        """
        return calculate_bmr(weight_kg, height_cm, age, sex)

    def convert_weight(self, weight, from_unit, to_unit):
        """
        Convert weight between kilograms and pounds.
        Args:
            weight (float): The weight to convert.
            from_unit (str): The current unit of the weight ('kg' or 'lbs').
            to_unit (str): The unit to convert the weight to ('kg' or 'lbs').
        Returns:
            float: Converted weight.
        """
        if from_unit == "kg" and to_unit == "lbs":
            return kg_to_lbs(weight)
        elif from_unit == "lbs" and to_unit == "kg":
            return lbs_to_kg(weight)
        else:
            return weight  # If the units are the same, return the original weight

    # More commands can be added here to handle other GUI actions.



'''
Explanation:

    Class Structure: The GUICommands class encapsulates all GUI-related commands.
      This organizes command handling neatly and makes it easy to extend.
    
    Initialization: It accepts API handlers and a database connection, which are
      stored as instance variables. This allows each command method to access APIs 
      and the database as needed.

    Method Examples: Methods like add_food_entry, fetch_nutritional_info,
      calculate_user_bmi, and convert_weight are implemented to handle specific 
      tasks that can be triggered from the GUI.
'''