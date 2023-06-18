from pprint import pprint

from test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterAchievementsAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_AchievementCategoriesIndex(self):
        self.BlizzardWarcraftAPI.get_CharacterAchievementsSummary("deepholm", "дъикиймвп")

    def test_CharacterAchievementStatistics(self):
        self.BlizzardWarcraftAPI.get_CharacterAchievementStatistics("deepholm", "дъикиймвп")
