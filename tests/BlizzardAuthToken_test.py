import os
from dotenv import load_dotenv
from unittest import TestCase
from BlizzardWarcraftAPI import BlizzardAuthToken

load_dotenv()


class Test_BlizzardAuthToken(TestCase):
    def test_getToken(self):
        b = BlizzardAuthToken(os.getenv("ClientID"), os.getenv("ClientSecret"))
        print(b.get())
