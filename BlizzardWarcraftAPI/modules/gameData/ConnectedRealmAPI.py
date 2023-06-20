from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class ConnectedRealmAPI(BlizzardWarcraftAPI):

    def get_ConnectedRealmsIndex(self) -> dict:
        """
        :return: Returns an index of connected realms.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/connected-realm/index"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

    def get_ConnectedRealm(self, connectedRealmId: int) -> dict:
        """
        :param connectedRealmId: The ID of the connected realm.
        :type connectedRealmId: int

        :return: Returns a connected realm by ID.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/connected-realm/{connectedRealmId}"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

    def get_ConnectedRealmsSearch(self, status_type: str, realms_timezone: str, orderby: str, page: int) -> dict:
        """
        For more detail see the Search Guide.
        https://develop.battle.net/documentation/world-of-warcraft/guides/search

        :param status_type: The status of the connected realm, UP or DOWN. (example search field)
        :param realms_timezone: The timezone of the realm. (example search field)
        :param orderby: The field to sort the result set by.
        :param page: The result page number.

        :type status_type: str
        :type realms_timezone: str
        :type orderby: str
        :type page: int

        :return: Performs a search of connected realms.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/search/connected-realm"
        self.param["namespace"] = self.namespace_dynamic
        self.param["status.type"] = status_type
        self.param["realms.timezone"] = realms_timezone
        self.param["orderby"] = orderby
        self.param["_page"] = page

        return self.response(url, self.param)