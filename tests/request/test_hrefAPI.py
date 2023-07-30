from pprint import pprint

from tests.test_base import BlizzardWarcraftAPI_test
from unittest import TestCase


class Test_AccountProfileAPI(BlizzardWarcraftAPI_test, TestCase):

    def test_request_href(self):
        href = "https://eu.api.blizzard.com/profile/wow/character/deepholm/%D0%B4%D1%8A%D0%B8%D0%BA%D0%B8%D0%B9?namespace=profile-eu"
        resp = self.Request.get_href(href)
        print(resp)