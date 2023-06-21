from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterEncountersAPI(BlizzardWarcraftAPI):

    def get_CharacterEncountersSummary(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of a character's encounters.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/encounters"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterDungeons(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of a character's completed dungeons.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/encounters" \
              f"/dungeons"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterRaids(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of a character's completed raids.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/encounters" \
              f"/raids"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)
