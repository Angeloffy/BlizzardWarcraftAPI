from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterHunterPetsAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterHunterPetsSummary(self):
        pprint(self.BlizzardWarcraftAPI.get_CharacterHunterPetsSummary("deepholm", "иъсихара"))