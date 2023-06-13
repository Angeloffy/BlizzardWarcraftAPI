import requests
from .BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class AchievementAPI(BlizzardWarcraftAPI):

    def __init__(self, BlizzardAuthToken, region: str, locale: str):
        super().__init__(BlizzardAuthToken, region, locale)
        self.param = {
            "namespace": self.namespace_static,
            "locale": self.locale,
            "access_token": self.BlizzardAuthToken
        }

    @staticmethod
    def response(url, param):
        resp = requests.get(url, params=param)
        return resp.json()

    def get_AchievementCategoriesIndex(self):
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement-category/index"
        return self.response(url, self.param)

    def get_AchievementCategory(self, achievementCategoryId: int):
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement-category/{achievementCategoryId}"
        return self.response(url, self.param)

    def get_AchievementsIndex(self):
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement/index"
        return self.response(url, self.param)

    def get_Achievement(self, achievementId):
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement/{achievementId}"
        return self.response(url, self.param)

    def get_AchievementMedia(self, achievementId):
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/achievement/{achievementId}"
        return self.response(url, self.param)
