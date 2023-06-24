from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class HeirloomAPI(BlizzardWarcraftAPI):

    def get_HeirloomIndex(self) -> dict:
        """
        :return: Returns an index of heirlooms.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/heirloom/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_Heirloom(self, heirloomId: int) -> dict:
        """
        :param heirloomId: The ID of the heirloom.
        :return: Returns an heirloom by id.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/heirloom/{heirloomId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)
