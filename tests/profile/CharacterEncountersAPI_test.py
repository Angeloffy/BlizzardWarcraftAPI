from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterEncountersAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterEncountersSummary(self):
        self.BlizzardWarcraftAPI.get_CharacterEncountersSummary("deepholm", "дъикиймвп")

    def test_CharacterDungeons(self):
        self.BlizzardWarcraftAPI.get_CharacterDungeons("deepholm", "дъикиймвп")

    def test_CharacterRaids(self):
        self.BlizzardWarcraftAPI.get_CharacterRaids("deepholm", "дъикиймвп")