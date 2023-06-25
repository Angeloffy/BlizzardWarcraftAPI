from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_JournalAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_JournalExpansionsIndex(self):
        self.GameData.get_JournalExpansionsIndex()

    def test_JournalExpansion(self):
        self.GameData.get_JournalExpansion(396)

    def test_JournalEncountersIndex(self):
        self.GameData.get_JournalEncountersIndex()

    def test_JournalEncounters(self):
        self.GameData.get_JournalEncounters(89)

    def test_JournalEncounterSearch(self):
        instance_name_en_US = "Deadmines"
        orderby = "id"
        page = 1
        self.GameData.get_JournalEncounterSearch(instance_name_en_US, orderby, page)

    def test_JournalInstancesIndex(self):
        self.GameData.get_JournalInstancesIndex()

    def test_JournalInstanceMedia(self):
        self.GameData.get_JournalInstanceMedia(63)