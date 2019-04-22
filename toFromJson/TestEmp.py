from toFromJson.Employee1 import Employee1
from toFromJson.Country1 import Country1


def checkEmp():
    emp = Employee1()
    emp._firstName = "DD"
    emp._lastName = "Mishra"
    country = Country1()
    country.countryCode = "12345"
    country.countryName = "India"
    emp.country = country

    print("Emp in toString format : ", emp.__dict__)
    print("--------------------- IN JSON -----------------")
    print(emp.toJSON())

    jsonString = '{ "_country": { "_countryCode": "7896", "_countryName": "India" }, "_firstName": "John", "_lastName": "Abrham" }'

    emp1 = emp.toEmployee(jsonString)
    print("Employee Name : ", emp1.firstName())
    print("Conveted object : ", emp1.__dict__)


if __name__ == "__main__":
    checkEmp()
