from test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_AchievementAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_AchievementCategoriesIndex(self):
        self.BlizzardWarcraftAPI.get_AchievementCategoriesIndex()

    def test_AchievementCategory(self):
        achievementId = 81
        self.BlizzardWarcraftAPI.get_AchievementCategory(achievementId)

    def test_AchievementsIndex(self):
        self.BlizzardWarcraftAPI.get_AchievementsIndex()

    def test_Achievement(self):
        achievementId = 6
        self.BlizzardWarcraftAPI.get_Achievement(achievementId)

    def test_AchievementMedia(self):
        achievementId = 6
        self.BlizzardWarcraftAPI.get_AchievementMedia(achievementId)
