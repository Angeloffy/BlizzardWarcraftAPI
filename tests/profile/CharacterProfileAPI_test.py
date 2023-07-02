from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterProfileAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterProfileSummary(self):
        pprint(self.Profile.get_CharacterProfileSummary("deepholm", "иъсихара"))

    def test_CharacterProfileStatus(self):
        pprint(self.Profile.get_CharacterProfileStatus("deepholm", "иъсихара"))