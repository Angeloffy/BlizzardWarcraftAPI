from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_ItemAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_ItemClassesIndex(self):
        self.GameData.get_ItemClassesIndex()

    def test_ItemClass(self):
        self.GameData.get_ItemClass(1)

    def test_ItemSetsIndex(self):
        self.GameData.get_ItemSetsIndex()

    def test_ItemSet(self):
        self.GameData.get_ItemSet(1)

    def test_ItemSubclass(self):
        self.GameData.get_ItemSubclass(1, 2)

    def test_Item(self):
        self.GameData.get_Item(19019)

    def test_ItemMedia(self):
        self.GameData.get_ItemMedia(19019)

    def test_ItemSearch(self):
        instance_name_en_US = "Deadmines"
        orderby = "id"
        page = 1
        self.GameData.get_ItemSearch(instance_name_en_US, orderby, page)
