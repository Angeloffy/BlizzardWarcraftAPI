from .modules import \
    AchievementAPI, AuctionHouseAPI, \
    ConnectedRealmAPI, CharacterAchievementsAPI, \
    CharacterAppearanceAPI


class BlizzardWarcraftAPI(AuctionHouseAPI, AchievementAPI,
                          ConnectedRealmAPI, CharacterAchievementsAPI,
                          CharacterAppearanceAPI):
    """
    Use BlizzardAuthToken class for generate access token.

    :param str BlizzardAuthToken: Access token.
    :param str region: The region of the data to retrieve.
    :param locale: The locale to reflect in localized data.

    :type BlizzardAuthToken: str
    :type region: str
    :type locale: str
    """
    def __init__(self, BlizzardAuthToken, region: str, locale: str):
        super().__init__(BlizzardAuthToken, region, locale)

