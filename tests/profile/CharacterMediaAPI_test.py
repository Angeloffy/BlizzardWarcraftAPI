from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterMediaAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterMediaSummary(self):
        pprint(self.Profile.get_CharacterMediaSummary("deepholm", "иъсихара"))