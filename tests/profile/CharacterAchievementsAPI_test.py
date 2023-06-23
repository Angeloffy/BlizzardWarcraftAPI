from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterAchievementsAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_AchievementCategoriesIndex(self):
        self.Profile.get_CharacterAchievementsSummary("deepholm", "дъикиймвп")

    def test_CharacterAchievementStatistics(self):
        self.Profile.get_CharacterAchievementStatistics("deepholm", "дъикиймвп")
