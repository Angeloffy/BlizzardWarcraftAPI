from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterCollectionsAPI(BlizzardWarcraftAPI):

    def get_CharacterCollectionsIndex(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns an index of collection types for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/collections"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterMountsCollectionSummary(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of the mounts a character has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/collections" \
              f"/mounts"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterPetsCollectionSummary(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of the battle pets a character has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/collections" \
              f"/pets"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterToysCollectionSummary(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of the toys a character has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/collections" \
              f"/toys"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterHeirloomsCollectionSummary(self, realmSlug, characterName) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of the heirlooms a character has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/collections" \
              f"/heirlooms"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)
