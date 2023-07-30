import requests
from ..data import region_data, locales_region_data
from ..exceptions import BlizzardWarcraftApiError
from ..urls import URL_TOKEN_VALIDATION


class BlizzardWarcraftAPI:
    @staticmethod
    def response(url, param):
        resp = requests.get(url, params=param)
        return resp.json()

    @staticmethod
    def __valid_region(region):
        if region in region_data:
            return True
        else:
            text = f"Region must be: {region_data}"
            raise BlizzardWarcraftApiError(text)

    @staticmethod
    def __valid_locale(region, locale):
        locales = locales_region_data.get(region)
        if locale in locales:
            return True
        else:
            text = f"Region must be for {region}: {locales}"
            raise BlizzardWarcraftApiError(text)

    @staticmethod
    def __valid_BlizzardAuthToken(token):
        data = {
            "token": token,
        }

        response = requests.post(URL_TOKEN_VALIDATION, data=data)
        response_data = response.json()

        if "error" not in response_data:
            return True
        else:
            text = response_data["error"] + " - " + response_data["error_description"]
            raise BlizzardWarcraftApiError(text)

    def __init__(self, BlizzardAuthToken, region: str, locale: str):

        if self.__valid_BlizzardAuthToken(BlizzardAuthToken):
            self.BlizzardAuthToken = BlizzardAuthToken

        region = region.lower()
        if self.__valid_region(region):
            self.region = region

        if self.__valid_locale(self.region, locale):
            self.locale = locale

        self.namespace_profile = "profile-" + self.region
        self.namespace_static = "static-" + self.region
        self.namespace_dynamic = "dynamic-" + self.region

        self.param = {
            "locale": self.locale,
            "access_token": self.BlizzardAuthToken
        }
