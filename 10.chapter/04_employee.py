class Employee:
    companay="google"
    salary=100

harry=Employee()
rajni=Employee()
harry.salary=300
rajni.salary=400

print(harry.companay)
print(rajni.companay)
Employee.companay="YouTube"

print(harry.companay)
print(rajni.companay)

print(harry.salary)
print(rajni.salary)

