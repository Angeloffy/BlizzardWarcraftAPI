class BlizzardAuthTokenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class BlizzardWarcraftApiError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
