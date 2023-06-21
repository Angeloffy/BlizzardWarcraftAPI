from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterEquipmentAPI(BlizzardWarcraftAPI):

    def get_CharacterEquipmentSummary(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of the items equipped by a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/equipment"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)