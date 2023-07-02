from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterProfileAPI(BlizzardWarcraftAPI):

    def get_CharacterProfileSummary(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a profile summary for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterProfileStatus(self, realmSlug: str, characterName: str) -> dict:
        """
        A client should delete information about a character from their application if any of the following conditions occur:
        - an HTTP 404 Not Found error is returned
        - the is_valid value is false
        - the returned character ID doesn't match the previously recorded value for the character

        The following example illustrates how to use this endpoint:

        1. A client requests and stores information about a character,
        including its unique character ID and the timestamp of the request.
        2. After 30 days,
        the client makes a request to the status endpoint to verify if the character information is still valid.
        3. If character cannot be found,
        is not valid, or the characters IDs do not match, the client removes the information from their application.
        4. If the character is valid and the character IDs match,
        the client retains the data for another 30 days.

        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns the status and a unique ID for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/status"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)
