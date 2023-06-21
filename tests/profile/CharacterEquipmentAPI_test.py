from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterEquipmentAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterEncountersSummary(self):
        self.BlizzardWarcraftAPI.get_CharacterEquipmentSummary("deepholm", "дъикиймвп")
