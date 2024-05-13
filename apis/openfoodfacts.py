import requests

class OpenFoodFactsAPI:
    def __init__(self, api_key=None):
        """
        Initialize the OpenFoodFacts API interface.
        :param api_key: API key for OpenFoodFacts if required (not generally needed as of now).
        """
        self.base_url = "https://world.openfoodfacts.org/api/v0/product"
        self.api_key = api_key

    def fetch_product(self, barcode):
        """
        Fetch product data by barcode.
        :param barcode: The barcode of the product to look up.
        :return: JSON response containing product data if found, else None.
        """
        url = f"{self.base_url}/{barcode}.json"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            product_data = response.json()
            if product_data.get('status') == 1:  # Status 1 means product found
                return product_data['product']
            else:
                print(f"Product with barcode {barcode} not found.")
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        return None

    # You can add more methods here to interact with different aspects of the API

'''
Explanation:
    Class Definition: The OpenFoodFactsAPI class encapsulates all the functionality
      needed to interact with the OpenFoodFacts API.

    Initialization: The __init__ method sets up any necessary configuration, such
      as the base URL for API requests. OpenFoodFacts API currently does not require
      an API key, but I included it in the constructor for future-proofing and 
      consistency with other API classes.
      
    Fetch Product: The fetch_product method retrieves the data for a specific
      product using its barcode. It makes an HTTP GET request and processes the 
      response, checking if the product is found and handling any errors that 
      occur during the request.

'''