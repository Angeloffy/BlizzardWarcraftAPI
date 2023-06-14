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

    def get_AchievementCategoriesIndex(self) -> dict:
        """
        :return: an index of achievement categories.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement-category/index"
        return self.response(url, self.param)

    def get_AchievementCategory(self, achievementCategoryId: int) -> dict:
        """
        :param achievementCategoryId: Achievement category id
        :type achievementCategoryId: int
        :return: an achievement category by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement-category/{achievementCategoryId}"
        return self.response(url, self.param)

    def get_AchievementsIndex(self) -> dict:
        """
        :return: an index of achievements.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement/index"
        return self.response(url, self.param)

    def get_Achievement(self, achievementId) -> dict:
        """
        :param achievementId: Achievement id
        :type achievementId: int
        :return: an achievement by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement/{achievementId}"
        return self.response(url, self.param)

    def get_AchievementMedia(self, achievementId) -> dict:
        """
        :param achievementId: Achievement id
        :type achievementId: int
        :return: media for an achievement by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/achievement/{achievementId}"
        return self.response(url, self.param)
