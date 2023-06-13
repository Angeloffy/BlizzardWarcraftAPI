from .modules import AchievementAPI


class BlizzardWarcraftAPI(AchievementAPI):
    """
    Use BlizzardAuthToken class for generate access token
    :param str BlizzardAuthToken: access_token
    :param str region: "us", "eu", "kr", "tw"
    :param locale: "en_US", "es_MX", "pt_BR", "en_GB",
            "es_ES", "fr_FR", "ru_RU", "de_DE",
            "pt_PT", "it_IT", "ko_KR","zh_TW"

    :type BlizzardAuthToken: str
    :type region: str
    :type locale: str
    """
    def __init__(self, BlizzardAuthToken, region: str, locale: str):
        super().__init__(BlizzardAuthToken, region, locale)

