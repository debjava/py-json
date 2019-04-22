import json


class Employee1:

    def __init__(self):
        self._firstName = None
        self._lastName = None
        self._country = None

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, fName):
        self._firstName = fName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lName):
        self._lastName = lName

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, contryObj):
        self._country = contryObj

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def toEmployee(self, jsonString):
        return json.loads(jsonString)
