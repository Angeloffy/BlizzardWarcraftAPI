import requests
from requests.models import Response
from BlizzardAuthToken import BlizzardAuthToken


class BlizzardWarcraftAPI():

    def __init__(self, ClientID: str, ClientSecret: str, region: str, locale: str = "en_GB"):
        self.ClientID: str = ClientID
        self.ClientSecret: str = ClientSecret
        self.region = region
        self.locale = locale
        self.BlizzardAuthToken = BlizzardAuthToken(self.ClientID, self.ClientSecret).get()

    @staticmethod
    def __request_get(url, data):
        print(requests.get(url, params=data).url)
        return requests.get(url, params=data)

    def get_CharacterAchievementsSummary(self, realmSlug: str, characterName: str) -> Response:
        data = {
            "namespace": "profile-eu",
            "locale": "ru_RU",
            "access_token": self.BlizzardAuthToken
        }
        url = f"https://eu.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName.lower()}/achievements"

        return self.__request_get(url, data)
