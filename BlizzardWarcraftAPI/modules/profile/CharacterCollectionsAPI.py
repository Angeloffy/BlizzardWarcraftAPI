from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterCollectionsAPI(BlizzardWarcraftAPI):

    def get_CharacterCollectionsIndex(self, realmSlug, characterName) -> dict:
        """
        :return: Returns an index of collection types for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/collections"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)