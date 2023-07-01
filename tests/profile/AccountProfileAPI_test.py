from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_AccountProfileAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_AchievementCategoriesIndex(self):
        self.Profile.get_CharacterAchievementsSummary("deepholm", "дъикиймвп")