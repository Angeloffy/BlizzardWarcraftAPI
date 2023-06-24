from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_HeirloomAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_HeirloomIndex(self):
        self.GameData.get_HeirloomIndex()

    def test_Heirloom(self):
        self.GameData.get_Heirloom(1)
