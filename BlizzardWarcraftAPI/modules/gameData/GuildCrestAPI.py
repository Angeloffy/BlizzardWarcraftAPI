from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class GuildCrestAPI(BlizzardWarcraftAPI):

    def get_GuildCrestComponentsIndex(self) -> dict:
        """
        :return: Returns an index of guild crest media.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/guild-crest/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_GuildCrestBorderMedia(self, borderId: int) -> dict:
        """
        :param borderId: The ID of the guild crest border.
        :return: Returns media for a guild crest border by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/guild-crest/border/{borderId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_GuildCrestEmblemMedia(self, emblemId: int) -> dict:
        """
        :param emblemId: The ID of the guild crest emblem.
        :return: Returns media for a guild crest emblem by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/guild-crest/emblem/{emblemId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)
