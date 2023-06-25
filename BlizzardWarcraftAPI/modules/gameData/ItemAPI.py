from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class ItemAPI(BlizzardWarcraftAPI):

    def get_ItemClassesIndex(self) -> dict:
        """
        :return: Returns an index of item classes.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/item-class/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_ItemClass(self, itemClassId: int) -> dict:
        """
        :param itemClassId: The ID of the item class.
        :return: Returns an item class by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/item-class/{itemClassId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_ItemSetsIndex(self) -> dict:
        """
        :return: Returns an index of item sets.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/item-set/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_ItemSet(self, itemSetId: int) -> dict:
        """
        :param itemSetId: The ID of the item set.
        :return: Returns an item set by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/item-set/{itemSetId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_ItemSubclass(self, itemClassId: int, itemSubclassId: int) -> dict:
        """
        :param itemClassId: The ID of the item class.
        :param itemSubclassId: The ID of the item subclass.
        :return: Returns an item subclass by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/item-class/{itemClassId}/item-subclass/{itemSubclassId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_Item(self, itemId: int) -> dict:
        """
        :param itemId: The ID of the item.
        :return: Returns an item by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/item/{itemId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_ItemMedia(self, itemId: int) -> dict:
        """
        :param itemId: The ID of the item.
        :return: Returns media for an item by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/item/{itemId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_ItemSearch(self, instance_name_en_US: str, orderby: str, page: int) -> dict:
        """
        Performs a search of items. The fields below are provided for example.
        https://develop.battle.net/documentation/world-of-warcraft/guides/search
        :param instance_name_en_US: The instance name where an encounter appears. (example search field)
        :param orderby: The field to sort the result set by.
        :param page: The result page number.
        :return: Returns media for an item by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/search/item"
        self.param["namespace"] = self.namespace_static
        self.param["instance.name.en_US"] = instance_name_en_US
        self.param["orderby"] = orderby
        self.param["_page"] = page
        return self.response(url, self.param)