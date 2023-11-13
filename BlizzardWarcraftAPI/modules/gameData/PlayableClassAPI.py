from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class PlayableClassAPI(BlizzardWarcraftAPI):

    def get_PlayableClassesIndex(self) -> dict:
        """
        :return: Returns an index of playable classes.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/playable-class/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_PlayableClass(self, classId: int) -> dict:
        """
        :return: Returns an index of playable classes.
        :param classId: The ID of the playable class.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/playable-class/{classId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_PlayableClassMedia(self, playableClassId: int) -> dict:
        """
        :return: Returns an index of playable classes.
        :param playableClassId: The ID of the playable class.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/playable-class/{playableClassId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_PvPTalentSlots(self, classId: int) -> dict:
        """
        :return: Returns an index of playable classes.
        :param classId: The ID of the playable class.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/playable-class/{classId}/pvp-talent-slots"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)
