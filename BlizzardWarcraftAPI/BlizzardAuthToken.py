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

    def get_wowProfile_scope(self, redirect_uri: str, state: str):
        authorize_url = "https://battle.net/oauth/authorize"
        client_id = self.ClientID
        scope = "wow.profile"
        response_type = "code"

        authorize_params = {
            "client_id": client_id,
            "scope": scope,
            "state": state,
            "redirect_uri": redirect_uri,
            "response_type": response_type,
        }

        authorize_request = requests.Request("GET", authorize_url, params=authorize_params)
        prepared_authorize_request = authorize_request.prepare()
        authorize_url_with_params = prepared_authorize_request.url

        return authorize_url_with_params

