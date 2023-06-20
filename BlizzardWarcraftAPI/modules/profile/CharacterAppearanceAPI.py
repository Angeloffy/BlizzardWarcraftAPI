from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterAppearanceAPI(BlizzardWarcraftAPI):

    def get_CharacterAppearanceSummary(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of a character's appearance settings.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/appearance"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)