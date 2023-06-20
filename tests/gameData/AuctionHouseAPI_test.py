from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_AuctionHouseAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_Auctions(self):
        self.BlizzardWarcraftAPI.get_Auctions(1305)

    def test_Commodities(self):
        self.BlizzardWarcraftAPI.get_Commodities()
