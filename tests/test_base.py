import os
from dotenv import load_dotenv
from BlizzardWarcraftAPI import BlizzardWarcraftAPI, BlizzardAuthToken

load_dotenv()


class BlizzardWarcraftAPI_test():
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        t = BlizzardAuthToken(os.getenv("ClientID"), os.getenv("ClientSecret"))
        self.token = t.get()
        self.region = "eu"
        self.locale = "en_GB"

        self.BlizzardWarcraftAPI = BlizzardWarcraftAPI(self.token, self.region, self.locale)
