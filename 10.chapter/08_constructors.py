class Employee:
    company="google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

    def getDetails(self):
        print(f"Employee name is {self.name}")
        print(f"Employee salary is {self.salary}")
        print(f"Employee subunit is {self.subunit}")


    def getSalary(self):
        print(f"salary for employee working in {self.company} is  {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning , bro")

    @staticmethod
    def time():
        print("time is 8pm")

harry=Employee("harry",10000,"YouTube")
harry.getDetails()