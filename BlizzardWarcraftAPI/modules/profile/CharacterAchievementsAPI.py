from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CharacterAchievementsAPI(BlizzardWarcraftAPI):

    def get_CharacterAchievementsSummary(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a summary of the achievements a character has completed.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/achievements"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)

    def get_CharacterAchievementStatistics(self, realmSlug: str, characterName: str) -> dict:
        """
        :param realmSlug: The slug of the realm.
        :param characterName: The lowercase name of the character.

        :return: Returns a character's statistics as they pertain to achievements.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/profile/wow/character/{realmSlug}/{characterName}/achievements/statistics"
        self.param["namespace"] = self.namespace_profile
        return self.response(url, self.param)