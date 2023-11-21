from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_PvPSeasonAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_PvPSeasonsIndex(self):
        self.GameData.get_PvPSeasonsIndex()

    def test_PvPSeasons(self):
        self.GameData.get_PvPSeasons(36)

    def test_PvPLeaderboardsIndex(self):
        self.GameData.get_PvPLeaderboardsIndex(36)

    def test_PvPLeaderboard(self):
        self.GameData.get_PvPLeaderboard(36, "2v2")

    def test_PvPRewardsIndex(self):
        self.GameData.get_PvPRewardsIndex(36)