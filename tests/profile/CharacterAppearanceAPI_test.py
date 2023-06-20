from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterAppearanceAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterAppearanceSummary(self):
        self.BlizzardWarcraftAPI.get_CharacterAppearanceSummary("deepholm", "дъикиймвп")
