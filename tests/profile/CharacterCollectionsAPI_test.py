from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_CharacterCollectionsAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_CharacterCollectionsIndex(self):
        self.Profile.get_CharacterCollectionsIndex("deepholm", "дъикиймвп")

    def test_CharacterMountsCollectionSummary(self):
        self.Profile.get_CharacterMountsCollectionSummary("deepholm", "дъикиймвп")

    def test_CharacterPetsCollectionSummary(self):
        self.Profile.get_CharacterPetsCollectionSummary("deepholm", "дъикиймвп")

    def test_CharacterToysCollectionSummary(self):
        self.Profile.get_CharacterToysCollectionSummary("deepholm", "дъикиймвп")

    def test_CharacterHeirloomsCollectionSummary(self):
        self.Profile.get_CharacterHeirloomsCollectionSummary("deepholm", "дъикиймвп")
