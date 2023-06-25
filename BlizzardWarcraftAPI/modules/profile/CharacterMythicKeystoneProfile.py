from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterMythicKeystoneProfile(BlizzardWarcraftAPI):

    def get_CharacterMythicKeystoneProfileIndex(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns the Mythic Keystone profile index for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/mythic" \
              f"-keystone-profile"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterMythicKeystoneSeasonDetails(self, realmSlug: str, characterName: str, seasonId: int) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.
        :param seasonId: The ID of the Mythic Keystone season.

        :return: Returns the Mythic Keystone season details for a character. Returns a 404 Not Found for characters that have not yet completed a Mythic Keystone dungeon for the specified season.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/mythic" \
              f"-keystone-profile/season/{seasonId}"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)