import requests
from requests_oauthlib import OAuth2Session

class FitbitAPI:
    def __init__(self, client_id, client_secret, redirect_uri):
        """
        Initialize the Fitbit API interface.
        :param client_id: Client ID for Fitbit API.
        :param client_secret: Client Secret for Fitbit API.
        :param redirect_uri: Redirect URI for OAuth authentication.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_url = "https://api.fitbit.com"
        self.token_url = "https://api.fitbit.com/oauth2/token"
        self.authorization_base_url = "https://www.fitbit.com/oauth2/authorize"
        self.scope = ["activity", "sleep", "heartrate", "profile"]
        self.oauth = OAuth2Session(client_id=self.client_id, redirect_uri=self.redirect_uri,
                                   scope=self.scope)
    
    def fetch_authorization_url(self):
        """
        Fetch the authorization URL to which the user must be redirected to give access.
        :return: URL for authorization.
        """
        authorization_url, state = self.oauth.authorization_url(self.authorization_base_url)
        return authorization_url, state

    def fetch_access_token(self, authorization_response):
        """
        Fetch the access token from Fitbit after the user authorizes the app.
        :param authorization_response: The full callback URL to which the user was redirected.
        :return: Access token.
        """
        token = self.oauth.fetch_token(self.token_url, authorization_response=authorization_response,
                                       client_secret=self.client_secret)
        return token

    def get_user_data(self, resource_type, date, user_id='-'):
        """
        Retrieve user data for a specified resource type and date.
        :param resource_type: Type of data to retrieve (e.g., 'activities/steps', 'sleep').
        :param date: Date for which data is requested, in the format 'YYYY-MM-DD'.
        :param user_id: User ID, default is '-' which refers to the current logged-in user.
        :return: JSON response with the requested data.
        """
        url = f"{self.base_url}/1/user/{user_id}/{resource_type}/date/{date}.json"
        headers = {"Authorization": f"Bearer {self.oauth.token['access_token']}"}
        response = requests.get(url, headers=headers)
        try:
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            return None

    # Add more methods here to interact with different parts of the Fitbit API


'''
Key Components:
    Class Definition: The FitbitAPI class encapsulates all functionalities needed
      to interact with Fitbit.

    OAuth Authentication: It handles the OAuth flow necessary to authenticate and
      authorize the application to access user data.

    Data Retrieval: The get_user_data method fetches data of a specified type for
      a particular user on a given date. It's designed to handle various types of 
      health data that Fitbit provides.

Considerations:
    Secure Storage: OAuth tokens should be stored securely, especially in a production environment.
    Error Handling: Basic error handling is included, but more comprehensive error management might be necessary, depending on the reliability requirements of your application.

'''