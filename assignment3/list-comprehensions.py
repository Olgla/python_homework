import csv

#Task 3: List Comprehensions Practice
with open("../csv/employees.csv", "r") as file:
    data = list(csv.reader(file))
    employees = data[1:]
    employee_names = [employee[1] + " " + employee[2] for employee in employees]
print(employee_names)

employee_name_e = [name for name in employee_names if "e" in name.lower()]
print(employee_name_e)
   