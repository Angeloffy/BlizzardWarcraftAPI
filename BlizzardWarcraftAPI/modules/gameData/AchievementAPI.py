import requests
from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class AchievementAPI(BlizzardWarcraftAPI):

    def get_AchievementCategoriesIndex(self) -> dict:
        """
        :return: an index of achievement categories.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement-category/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_AchievementCategory(self, achievementCategoryId: int) -> dict:
        """
        :param achievementCategoryId: The ID of the achievement category.
        :type achievementCategoryId: int
        :return: an achievement category by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement-category/{achievementCategoryId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_AchievementsIndex(self) -> dict:
        """
        :return: an index of achievements.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_Achievement(self, achievementId) -> dict:
        """
        :param achievementId: The ID of the achievement category.
        :type achievementId: int
        :return: an achievement by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/achievement/{achievementId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_AchievementMedia(self, achievementId) -> dict:
        """
        :param achievementId: The ID of the achievement category.
        :type achievementId: int
        :return: media for an achievement by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/achievement/{achievementId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)
