from .modules import *


class BlizzardWarcraftAPI:
    """
    Use BlizzardAuthToken class for generate access token.

    :param str BlizzardAuthToken: Access token.
    :param str region: The region of the data to retrieve.
    :param locale: The locale to reflect in localized data.

    :type BlizzardAuthToken: str
    :type region: str
    :type locale: str
    """
    def __init__(self, BlizzardAuthToken: str, region: str, locale: str):
        BlizzardWarcraftAPI.BlizzardAuthToken = BlizzardAuthToken
        BlizzardWarcraftAPI.region = region
        BlizzardWarcraftAPI.locale = locale

    class GameData(AchievementAPI, AuctionHouseAPI,
                   ConnectedRealmAPI, CreatureAPI,
                   GuildCrestAPI, HeirloomAPI,
                   JournalAPI, ItemAPI):
        """
        The World of Warcraft game data APIs encompass both static and dynamic game data.
        https://develop.battle.net/documentation/world-of-warcraft/game-data-apis
        """
        def __init__(self):
            super().__init__(BlizzardWarcraftAPI.BlizzardAuthToken, BlizzardWarcraftAPI.region, BlizzardWarcraftAPI.locale)

    class Profile(CharacterAchievementsAPI, CharacterCollectionsAPI,
                  CharacterEquipmentAPI, CharacterEncountersAPI,
                  CharacterHunterPetsAPI, CharacterAppearanceAPI,
                  CharacterMediaAPI, CharacterProfessionsAPI,
                  CharacterMythicKeystoneProfile, AccountProfileAPI,
                  CharacterProfileAPI, CharacterPvPAPI):
        """
        The World of Warcraft profile APIs listed below encompass profile game data.
        https://develop.battle.net/documentation/world-of-warcraft/profile-apis
        """
        def __init__(self):
            super().__init__(BlizzardWarcraftAPI.BlizzardAuthToken, BlizzardWarcraftAPI.region, BlizzardWarcraftAPI.locale)

    class Request(hrefAPI):
        
        def __init__(self):
            super().__init__(BlizzardWarcraftAPI.BlizzardAuthToken, BlizzardWarcraftAPI.region, BlizzardWarcraftAPI.locale)

