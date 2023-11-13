from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_PlayableClassesIndex(BlizzardWarcraftAPI_test, TestCase):

    def test_JournalExpansionsIndex(self):
        self.GameData.get_PlayableClassesIndex()

    def test_PlayableClass(self):
        self.GameData.get_PlayableClass(3)

    def test_PlayableClassMedia(self):
        self.GameData.get_PlayableClassMedia(3)

    def test_PvPTalentSlots(self):
        self.GameData.get_PvPTalentSlots(3)
