import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class GoogleFitAPI:
    def __init__(self, client_id, client_secret):
        """
        Initialize the Google Fit API interface.
        :param client_id: Client ID for Google API.
        :param client_secret: Client Secret for Google API.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://www.googleapis.com/fitness/v1"
        self.token_url = "https://oauth2.googleapis.com/token"
        self.scopes = ["https://www.googleapis.com/auth/fitness.activity.read"]
        self.token = self.authenticate()

    def authenticate(self):
        """
        Authenticate with the Google API using OAuth 2.0
        :return: Token for the session.
        """
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client, scope=self.scopes)
        return oauth.fetch_token(token_url=self.token_url, client_id=self.client_id,
                                 client_secret=self.client_secret)

    def get_activity_data(self, user_id, data_source, start_time, end_time):
        """
        Retrieve activity data from Google Fit.
        :param user_id: ID of the user whose data is being fetched.
        :param data_source: Type of activity data to fetch (e.g., 'steps', 'calories').
        :param start_time: Start time for data retrieval, in milliseconds since epoch.
        :param end_time: End time for data retrieval, in milliseconds since epoch.
        :return: JSON response containing the activity data.
        """
        url = f"{self.base_url}/users/{user_id}/dataset:aggregate"
        headers = {
            "Authorization": f"Bearer {self.token['access_token']}",
            "Content-Type": "application/json"
        }
        body = {
            "aggregateBy": [{"dataTypeName": data_source}],
            "bucketByTime": {"durationMillis": (end_time - start_time)},
            "startTimeMillis": start_time,
            "endTimeMillis": end_time
        }
        response = requests.post(url, headers=headers, json=body)
        try:
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    # Add more methods here to interact with different parts of the Google Fit API

'''
Key Components:
    Class Definition: The GoogleFitAPI class encapsulates the interactions with Google Fit.

    Authentication: Uses OAuth 2.0 for secure access to user data.
      The authenticate method handles the token fetching process using client credentials.

    Data Retrieval: The get_activity_data method allows fetching various types
      of fitness data. It's designed to be flexible with parameters for user ID,
      data source type, and time range.

Note:
    OAuth and Permissions: Handling OAuth properly requires securely storing
      credentials and tokens, potentially using a more secure storage mechanism
      depending on your application's deployment.
      
    Error Handling: Basic error handling is included, but you may want to expand
      this to handle specific error codes or retry logic.

'''