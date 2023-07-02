from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterPvPAPI(BlizzardWarcraftAPI):

    def get_CharacterPvPBracketStatistics(self, realmSlug: str, characterName: str, pvpBracket: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.
        :param pvpBracket: The PvP bracket type.

        :return: Returns the PvP bracket statistics for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/" \
              f"character/{realmSlug}/{characterName}/pvp-bracket/{pvpBracket}"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterPvPSummary(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns the PvP bracket statistics for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/pvp-summary"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)
