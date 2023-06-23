from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_AchievementAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_AchievementCategoriesIndex(self):
        self.GameData.get_AchievementCategory(1)

    def test_AchievementCategory(self):
        achievementId = 81
        self.GameData.get_AchievementCategory(achievementId)

    def test_AchievementsIndex(self):
        self.GameData.get_AchievementsIndex()

    def test_Achievement(self):
        achievementId = 6
        self.GameData.get_Achievement(achievementId)

    def test_AchievementMedia(self):
        achievementId = 6
        self.GameData.get_AchievementMedia(achievementId)
