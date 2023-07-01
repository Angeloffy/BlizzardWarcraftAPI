import requests
from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class AccountProfileAPI(BlizzardWarcraftAPI):

    def get_AccountProfileSummary(self) -> dict:
        """
        Because this endpoint provides data about the current logged-in user's World of Warcraft account,
        it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.\
        https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow

        :return: Returns a profile summary for an account.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/user/wow"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_ProtectedCharacterProfileSummary(self, realmId: int, characterId: int) -> dict:
        """
        Because this endpoint provides data about the current logged-in user's World of Warcraft account,
        it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.
        https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow

        :param realmId: The ID of the character's realm.
        :param characterId: The ID of the character.

        :return: Returns a protected profile summary for a character.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/user/wow/protected-character/{realmId}-{characterId}"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_AccountCollectionsIndex(self) -> dict:
        """
        Because this endpoint provides data about the current logged-in user's World of Warcraft account,
        it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.
        https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow

        :return: Returns an index of collection types for an account.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/user/wow/collections"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_AccountMountsCollectionSummary(self) -> dict:
        """
        Because this endpoint provides data about the current logged-in user's World of Warcraft account,
        it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.
        https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow

        :return: Returns a summary of the mounts an account has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/user/wow/collections/mounts"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_AccountPetsCollectionSummary(self) -> dict:
        """
        Because this endpoint provides data about the current logged-in user's World of Warcraft account,
        it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.
        https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow

        :return: Returns a summary of the battle pets an account has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/user/wow/collections/pets"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_AccountToysCollectionSummary(self) -> dict:
        """
        Because this endpoint provides data about the current logged-in user's World of Warcraft account,
        it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.
        https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow

        :return: Returns a summary of the toys an account has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/user/wow/collections/toys"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_AccountHeirloomsCollectionSummary(self) -> dict:
        """
        Because this endpoint provides data about the current logged-in user's World of Warcraft account,
        it requires an access token with the wow.profile scope acquired via the Authorization Code Flow.
        https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow

        :return: Returns a summary of the heirlooms an account has obtained.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/user/wow/collections/heirlooms"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)