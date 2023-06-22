from typing import Final

URL: Final[str] = "https://eu.battle.net"

# BlizzardAuthToken
URL_ACCESS_TOKEN_REQUEST: Final[str] = "%s/oauth/token" % URL
URL_TOKEN_VALIDATION: Final[str] = "%s/oauth/check_token" % URL

# Account Profile API
URL_ACCOUNT_PROFILE_SUMMARY: Final[str] = "%s/profile/user/wow" % URL

# Character Achievements API
URL_CHARACTER_ACHIEVEMENTS_SUMMARY: Final[str] = "%s/profile/wow/character/" % URL
