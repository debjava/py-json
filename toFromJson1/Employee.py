import json


class Employee:
    def __init__(self, firstName=None, lastName=None, country=None):
        self.firstName = firstName
        self.lastName = lastName
        self.country = country


class Country:
    def __init__(self, countryName=None, countryCode=None):
        self.countryName = countryName
        self.countryCode = countryCode


def to_json(obj):
    if isinstance(obj, Employee):
        return {
            'firstName': obj.firstName,
            'lastName': obj.lastName,
            'country': obj.country,
        }
    if isinstance(obj, Country):
        return {
            'countryName': obj.countryName,
            'countryCode': obj.countryCode,
        }
    raise TypeError


def from_json(obj):
    if 'firstName' in obj:
        return Employee(**obj)
    if 'countryName' in obj:
        return Country(**obj)
    return obj


def check_emp():
    emp = Employee("DD", "Mishra", Country("India", "12345"))
    json_string = json.dumps(emp, default=to_json, sort_keys=True, indent=4)
    print(json_string)

    k = '{ "country": { "countryCode": "12345", "countryName": "India" }, "firstName": "DD", "lastName": "Mishra" }'

    # emp1 = json.loads(json_string, object_hook=from_json)
    emp1 = json.loads(k, object_hook=from_json)
    print("Employee Name : ", emp1.firstName)
    print("Employee Last Name : ", emp1.lastName)


if __name__ == "__main__":
    check_emp()

# Reference
# https://stackoverflow.com/questions/55775629/attributeerror-dict-object-has-no-attribute-while-converting-json-string-to-p/55776555#55776555