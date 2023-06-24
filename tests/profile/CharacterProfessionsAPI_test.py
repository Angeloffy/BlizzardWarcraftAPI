from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterProfessionsAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterProfessionsSummary(self):
        pprint(self.Profile.get_CharacterProfessionsSummary("deepholm", "иъсихара"))