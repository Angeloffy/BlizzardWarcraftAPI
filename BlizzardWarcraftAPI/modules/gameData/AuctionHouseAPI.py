from BlizzardWarcraftAPI.modules.BlizzardWarcraftAPI_base import BlizzardWarcraftAPI


class AuctionHouseAPI(BlizzardWarcraftAPI):

    def get_Auctions(self, connectedRealmId) -> dict:
        """
        See the Connected Realm API for information about retrieving a list of connected realm IDs.
        Auction house data updates at a set interval. The value was initially set at 1 hour; however, it might change
        over time without notice.
        Depending on the number of active auctions on the specified connected realm, the response from this endpoint may
        be rather large, sometimes exceeding 10 MB.

        :param connectedRealmId: The ID of the connected realm.
        :return: Returns all active auctions for a connected realm.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/connected-realm/{connectedRealmId}/auctions"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)

    def get_Commodities(self) -> dict:
        """
        Auction house data updates at a set interval. The value was initially set at 1 hour; however,
        it might change over time without notice.
        Depending on the number of active auctions on the specified connected realm,
        the response from this endpoint may be rather large, sometimes exceeding 10 MB.

        :return: Returns all active auctions for commodity items for the entire game region.
        :rtype: dict
        """
        url = f"https://{self.region}.api.blizzard.com/data/wow/auctions/commodities"
        self.param["namespace"] = self.namespace_dynamic
        return self.response(url, self.param)
