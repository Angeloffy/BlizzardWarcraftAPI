from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_PlayableRaceAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_PlayableRacesIndex(self):
        self.GameData.get_PlayableRacesIndex()

    def test_PlayableRace(self):
        self.GameData.get_PlayableRace(1)