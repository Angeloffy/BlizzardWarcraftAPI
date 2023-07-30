import requests
from requests import Response

from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class hrefAPI(BlizzardWarcraftAPI):

    def get_href(self, href) -> dict:
        """
        :return: Returns from href
        :rtype: dict
        """

        resp = requests.get(href, params=self.param)
        return resp.json()
