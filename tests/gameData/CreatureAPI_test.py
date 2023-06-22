from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CreatureAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CreatureFamiliesIndex(self):
        self.BlizzardWarcraftAPI.get_CreatureFamiliesIndex()

    def test_CreatureFamilies(self):
        self.BlizzardWarcraftAPI.get_CreatureFamily(1)

    def test_CreatureTypesIndex(self):
        self.BlizzardWarcraftAPI.get_CreatureTypesIndex()

    def test_CreatureType(self):
        self.BlizzardWarcraftAPI.get_CreatureType(1)

    def test_Creature(self):
        self.BlizzardWarcraftAPI.get_Creature(42722)

    def test_CreatureSearch(self):
        self.BlizzardWarcraftAPI.get_CreatureSearch("Dragon", "id", 1)

    def test_CreatureDisplayMedia(self):
        self.BlizzardWarcraftAPI.get_CreatureDisplayMedia(30221)

    def test_CreatureFamilyMedia(self):
        pprint(self.BlizzardWarcraftAPI.get_CreatureFamilyMedia(1))
