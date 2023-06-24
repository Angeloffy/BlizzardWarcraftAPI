from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterProfessionsAPI(BlizzardWarcraftAPI):

    def get_CharacterProfessionsSummary(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of professions for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/professions"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)