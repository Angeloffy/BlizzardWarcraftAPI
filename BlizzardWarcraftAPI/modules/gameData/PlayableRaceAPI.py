import requests
from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class PlayableRaceAPI(BlizzardWarcraftAPI):

    def get_PlayableRacesIndex(self) -> dict:
        """
        :return: Returns an index of playable races.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/playable-race/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_PlayableRace(self, playableRaceId: int) -> dict:
        """
        :return: Returns a playable race by ID.
        :param playableRaceId: The ID of the playable race.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/playable-race/{playableRaceId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)