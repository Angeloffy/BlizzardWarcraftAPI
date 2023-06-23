from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_AuctionHouseAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_ConnectedRealmsIndex(self):
        self.GameData.get_ConnectedRealmsIndex()

    def test_ConnectedRealm(self):
        self.GameData.get_ConnectedRealm(1080)

    def test_ConnectedRealmsSearch(self):
        self.GameData.get_ConnectedRealmsSearch("UP", "America/New_York", "id", 1)
