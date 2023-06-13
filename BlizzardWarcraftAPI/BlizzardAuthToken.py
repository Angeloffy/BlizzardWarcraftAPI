import requests
from .urls import URL_ACCESS_TOKEN_REQUEST
from .exceptions import BlizzardAuthTokenError


class BlizzardAuthToken():
    def __init__(self, ClientID: str, ClientSecret: str):
        """
        Get from https://develop.battle.net/access/clients

        :param str ClientID:
        :param str ClientSecret:
        """
        self.grant_type: str = "client_credentials"
        self.ClientID: str = ClientID
        self.ClientSecret: str = ClientSecret

    def get(self):
        data = {
            "grant_type": self.grant_type,
            "client_id": self.ClientID,
            "client_secret": self.ClientSecret,
        }

        response = requests.post(URL_ACCESS_TOKEN_REQUEST, data=data)
        response_data = response.json()

        if "error" not in response_data:
            return response_data["access_token"]
        else:
            text = response_data["error"] + " - " + response_data["error_description"]
            raise BlizzardAuthTokenError(text)
