import json
from threading                              import Thread


class JSONData(Thread):

    def __init__(self, employee, employee_not_today, call, emp_list=None, emp_na_list=None):
        super(JSONData, self).__init__()
        self.call                = call
        self.employee            = employee
        self.employee_not_today  = employee_not_today
        self.employees_list      = emp_list
        self.employees_na_list   = emp_na_list

    def run(self):
        if self.employees_list and self.call == 'Y':
            self.write_wished_employees_to_json()
        if self.employees_na_list and self.call == 'N':
            self.write_not_celebrating_employees_to_json()

    @staticmethod
    def extract_employee_data():
        with open(f"db/employees.json") as employees_file:
            employees = json.load(employees_file)
            return employees

    @staticmethod
    def extract_exc_employee_data():
        with open(f"db/exc_employees.json") as employees_file:
            exc_employees = json.load(employees_file)
            return exc_employees

    def write_wished_employees_to_json(self):
        with open('db/employees.json', 'w') as employees_file:
            json.dump(self.employees_list, employees_file)

    def write_not_celebrating_employees_to_json(self):
        with open('db/employees_na.json', 'w') as employees_not_today_file:
            json.dump(self.employees_na_list, employees_not_today_file)
