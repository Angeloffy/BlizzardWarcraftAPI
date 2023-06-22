from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class CreatureAPI(BlizzardWarcraftAPI):

    def get_CreatureFamiliesIndex(self) -> dict:
        """
        :return: Returns an index of creature families.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/creature-family/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_CreatureFamily(self, creatureFamilyId: int) -> dict:
        """
        :param creatureFamilyId: The ID of the creature family.
        :return: Returns a creature family by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/creature-family/{creatureFamilyId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_CreatureTypesIndex(self) -> dict:
        """
        :return: Returns an index of creature types.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/creature-type/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_CreatureType(self, creatureTypeId: int) -> dict:
        """
        :param creatureTypeId: The ID of the creature type.
        :return: Returns an index of creature types.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/creature-type/{creatureTypeId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_Creature(self, creatureId: int) -> dict:
        """
        :param creatureId: The ID of the creature.
        :return: Returns a creature by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/creature/{creatureId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_CreatureSearch(self, name_en_US: str, orderby: str, page: int) -> dict:
        """
        The fields below are provided for example. For more detail see the Search Guide.
        https://develop.battle.net/documentation/world-of-warcraft/guides/search
        :param name_en_US: The name of the creature. (example search field)
        :param orderby: The field to sort the result set by.
        :param page: The result page number.
        :return: Performs a search of creatures.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/search/creature"
        self.param["namespace"] = self.namespace_static
        self.param["name.en_US"] = name_en_US
        self.param["orderby"] = orderby
        self.param["_page"] = page

        return self.response(url, self.param)

    def get_CreatureDisplayMedia(self, creatureDisplayId: str) -> dict:
        """
        :param creatureDisplayId: The ID of the creature display.
        :return: Returns media for a creature display by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/creature-display/{creatureDisplayId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_CreatureFamilyMedia(self, creatureFamilyId: str) -> dict:
        """
        :param creatureFamilyId: The ID of the creature family.
        :return: Returns media for a creature family by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/creature-family/{creatureFamilyId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)