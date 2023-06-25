from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterMythicKeystoneProfile(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterMythicKeystoneProfileIndex(self):
        pprint(self.Profile.get_CharacterMythicKeystoneProfileIndex("deepholm", "иъсихара"))

    def test_CharacterMythicKeystoneSeasonDetails(self):
        pprint(self.Profile.get_CharacterMythicKeystoneSeasonDetails("deepholm", "иъсихара", 20))