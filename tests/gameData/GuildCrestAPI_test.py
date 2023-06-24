from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_GuildCrestAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_GuildCrestComponentsIndex(self):
        self.GameData.get_GuildCrestComponentsIndex()

    def test_GuildCrestBorderMedia(self):
        self.GameData.get_GuildCrestBorderMedia(0)

    def test_GuildCrestEmblemMedia(self):
        self.GameData.get_GuildCrestEmblemMedia(0)