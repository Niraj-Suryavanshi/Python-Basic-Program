class Employee:
    company="google"
    def getSalary(self):
        print(f"salary for employee working in {self.company} is  {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning , bro")

    @staticmethod
    def time():
        print("time is 8pm")

            


harry=Employee()
harry.salary=10000
harry.getSalary()
harry.greet()
harry.time()
# Employee.getSalary(harry)

        