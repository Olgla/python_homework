import csv
import os
import custom_module
from datetime import datetime

# print("PATH: ")
# print("cwd:", os.getcwd())
# print("exists:", os.path.exists("../csv/employees.csv"))

#Task 2: Read a CSV File
def read_employees():
    list = []
    dict = {}

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    dict["fields"] = row
                else:
                    list.append(row)
            dict["rows"] = list
        return dict
    except Exception as e:
        print(e)
        raise
            
employees = read_employees()

# print("TASK1")
# print(employees)


#Task 3: Find the Column Index
def column_index(str):
    return employees["fields"].index(str)

employee_id_column = column_index("employee_id")
# print(employee_id_column)


#Task 4: Find the Employee First Name
def first_name(rowNum):
    first_name_column = column_index("first_name")
    return employees["rows"][rowNum][first_name_column]
# print(first_name(2))


#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches
# print(employee_find(1))


#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    # last_name_column = column_index("last_name")
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]

# sort_by_last_name()
# print(employees)


# Task 8: Create a dict for an Employee
def employee_dict(row):
    keys = employees["fields"][1:]
    values = row[1:]
    return dict(zip(keys, values))

print(employee_dict(employees["rows"][1]))


#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    allEmployees = {}
    for row in employees["rows"]:
        employee_id = row[0]
        allEmployees[employee_id] = employee_dict(row)
    return allEmployees

# print("TASK9")
# print(all_employees_dict())


#Task 10: Use the os Module
def get_this_value():
    path_variable = os.environ.get('THISVALUE')
    return path_variable

# print(get_this_value())


#Task 11: Creating Your Own Module
def set_that_secret(newSecret):
    custom_module.set_secret(newSecret)
    print(newSecret)

# set_that_secret("happy")


#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes(filePath):
    list = []
    dict = {}

    try:
        with open(filePath, "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    dict["fields"] = row
                else:
                    list.append(tuple(row))
            dict["rows"] = list
        return dict
    except Exception as e:
        print(e)
        raise
            
minutes1 = read_minutes("../csv/minutes1.csv")
minutes2 = read_minutes("../csv/minutes2.csv")

# print(minutes1)
# print("2-------------")
# print(minutes2)


#Task 13: Create minutes_set
def create_minutes_set():
    total_minutes = set(minutes1["rows"]).union(set(minutes2["rows"]))
    return total_minutes

minutes_set = create_minutes_set()


#Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    records = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    return list(records) #to get the list instead of map iterator object, initiate list creation
    
minutes_list = create_minutes_list()
print(minutes_list)


#Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list)
    converted_list = list(converted)

    with open("./minutes.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"]) 
        writer.writerows(converted_list)

    return converted_list

write_sorted_list()