# __init__.py for the apis package

# Import the API handler classes
from .openfoodfacts import OpenFoodFactsAPI
from .google_fit import GoogleFitAPI
from .fitbit import FitbitAPI

# Optionally, you can define an initialization function to configure all APIs
def init_apis(config):
    """
    Initialize all API handlers with their respective configurations.
    :param config: A dictionary containing configuration settings for each API.
    :return: Dictionary of initialized API handlers.
    """
    openfoodfacts_api = OpenFoodFactsAPI()
    google_fit_api = GoogleFitAPI(client_id=config['GOOGLE_FIT_CLIENT_ID'],
                                  client_secret=config['GOOGLE_FIT_CLIENT_SECRET'])
    fitbit_api = FitbitAPI(client_id=config['FITBIT_CLIENT_ID'],
                           client_secret=config['FITBIT_CLIENT_SECRET'],
                           redirect_uri=config['FITBIT_REDIRECT_URI'])
    
    return {
        'openfoodfacts': openfoodfacts_api,
        'google_fit': google_fit_api,
        'fitbit': fitbit_api
    }

# You can also define any utility functions or constants that are used across your API modules

'''
Key Components:

    Imports: This file imports the main classes or functions from each of the submodules.
    This way, when you import the API package elsewhere in your application, you
    can access these elements directly through the package without needing to know
    which specific file they come from.

    Initialization Function: The init_apis function is an example of how you might
    initialize all your APIs at once. This is especially useful if your APIs need
    API keys or other configuration data passed at runtime. You could extend this
    pattern with more sophisticated setup or error handling as needed.

    Simplifying Imports: By defining what is imported by default from the package
    (__init__.py can include __all__ = ['OpenFoodFactsAPI', 'GoogleFitAPI', 'FitbitAPI', 'init_apis']),
    you can control the namespace of the package and avoid importing unnecessary
    submodules into the global namespace of modules that use this package.
'''