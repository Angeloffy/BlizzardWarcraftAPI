from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterPvPAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterPvPBracketStatistics(self):
        pprint(self.Profile.get_CharacterPvPBracketStatistics("deepholm", "дъикиймвп", "3v3"))

    def test_CharacterPvPSummary(self):
        pprint(self.Profile.get_CharacterPvPSummary("deepholm", "дъикиймвп"))