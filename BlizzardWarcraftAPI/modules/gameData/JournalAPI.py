from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class JournalAPI(BlizzardWarcraftAPI):

    def get_JournalExpansionsIndex(self) -> dict:
        """
        :return: Returns an index of journal expansions.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/journal-expansion/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_JournalExpansion(self, journalExpansionId: int) -> dict:
        """
        :param journalExpansionId: The ID of the journal expansion.
        :return: Returns a journal expansion by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/journal-expansion/{journalExpansionId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_JournalEncountersIndex(self) -> dict:
        """
        :return: Returns an index of journal encounters.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/journal-encounter/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_JournalEncounters(self, journalEncounterId: int) -> dict:
        """
        :param journalEncounterId: Returns a journal encounter by ID.
        :return: Returns a journal expansion by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/journal-encounter/{journalEncounterId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_JournalEncounterSearch(self, instance_name_en_US: str, orderby: str, page: int) -> dict:
        """
        Performs a search of journal encounters. The fields below are provided for example.
        https://develop.battle.net/documentation/world-of-warcraft/guides/search

        :param instance_name_en_US: The instance name where an encounter appears. (example search field)
        :param orderby: The field to sort the result set by.
        :param page: The result page number.
        :return:

        :return: Returns a journal expansion by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/search/journal-encounter"
        self.param["namespace"] = self.namespace_static
        self.param["instance.name.en_US"] = instance_name_en_US
        self.param["orderby"] = orderby
        self.param["_page"] = page

        return self.response(url, self.param)

    def get_JournalInstancesIndex(self) -> dict:
        """
        :return: Returns an index of journal instances.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/journal-instance/index"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)

    def get_JournalInstanceMedia(self, journalInstanceId: int) -> dict:
        """
        :param journalInstanceId: The ID of the journal instance.
        :return: Returns a journal expansion by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/media/journal-instance/{journalInstanceId}"
        self.param["namespace"] = self.namespace_static
        return self.response(url, self.param)
