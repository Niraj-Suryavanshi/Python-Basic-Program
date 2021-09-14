class Employee:
    company="google"
    salary=100

harry=Employee()
rajni=Employee()

harry.salary=300
rajni.salary=400

harry.salary=466
print(harry.salary)
print(rajni.salary)

# print(rajni.address)addree is not present so error will occure