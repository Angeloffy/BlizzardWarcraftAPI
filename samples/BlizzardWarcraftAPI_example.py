from BlizzardWarcraftAPI import BlizzardWarcraftAPI

api = BlizzardWarcraftAPI("token", "region", "locale")
GameData = api.GameData()
Profile = api.Profile()

GameData.get_AchievementCategory(1)
Profile.get_CharacterHunterPetsSummary("ravencrest", "bicmex")
