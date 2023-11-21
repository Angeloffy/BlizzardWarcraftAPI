from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class PvPSeasonAPI(BlizzardWarcraftAPI):

    def get_PvPSeasonsIndex(self) -> dict:
        """
        :return: Returns an index of PvP seasons.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/pvp-season/index"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

    def get_PvPSeasons(self, pvpSeasonId: int) -> dict:
        """
        :return: Returns a PvP season by ID.
        :param pvpSeasonId: The ID of the PvP season.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/pvp-season/{pvpSeasonId}"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

    def get_PvPLeaderboardsIndex(self, pvpSeasonId: int) -> dict:
        """
        :return: Returns an index of PvP leaderboards for a PvP season.
        :param pvpSeasonId: The ID of the PvP season.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/index"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

    def get_PvPLeaderboard(self, pvpSeasonId:int, pvpBracket: int) -> dict:
        """
        :return: Returns the PvP leaderboard of a specific PvP bracket for a PvP season.
        :param pvpSeasonId: The ID of the PvP season.
        :param pvpBracket: The PvP bracket type.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/pvp-season/{pvpSeasonId}/pvp-leaderboard/{pvpBracket}"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

    def get_PvPRewardsIndex(self, pvpSeasonId:int) -> dict:
        """
        :return: Returns an index of PvP rewards for a PvP season.
        :param pvpSeasonId: The ID of the PvP season.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/pvp-season/{pvpSeasonId}/pvp-reward/index"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

