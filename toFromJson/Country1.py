class Country1:
    def __init__(self):
        self._countryName = None
        self._countryCode = None

    @property
    def countryName(self):
        return self._countryName

    @countryName.setter
    def countryName(self, cName):
        self._countryName = cName

    @property
    def countryCode(self):
        return self._countryCode

    @countryCode.setter
    def countryCode(self, cCode):
        self._countryCode = cCode
