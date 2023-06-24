from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterMediaAPI(BlizzardWarcraftAPI):

    def get_CharacterMediaSummary(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of the media assets available for a character (such as an avatar render).
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/character-media"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)
