from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterHunterPetsAPI(BlizzardWarcraftAPI):

    def get_CharacterHunterPetsSummary(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: If the character is a hunter, returns a summary of the character's hunter pets. Otherwise, returns an HTTP 404 Not Found error.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/hunter-pets"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)