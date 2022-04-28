import json
import pathlib
from threading                              import Thread


class JSONData(Thread):
    """
    Threaded Class to process data without disrupting the process of the application
    Reads and writes json from/to files when called
    """

    __current_dir = pathlib.Path(__file__).parent

    def __init__(self, employee, employee_not_today, call, emp_list=None, emp_na_list=None):
        super(JSONData, self).__init__()
        self.call               = call
        self.employee           = employee
        self.employee_not_today = employee_not_today
        self.employees_list     = emp_list
        self.employees_na_list  = emp_na_list
        self.db_dir             = f'{self.__current_dir}/db'

    def run(self):
        """Start the thread's activity.

        It must be called at most once per thread object. It arranges for the
        object's run() method to be invoked in a separate thread of control.

        This method will raise a RuntimeError if called more than once on the
        same thread object.

        """
        if self.employees_list and self.call == 'Y':
            self.write_wished_employees_to_json()
        if self.employees_na_list and self.call == 'N':
            self.write_not_celebrating_employees_to_json()

    @staticmethod
    def extract_employee_data(json_file):
        """
        Reads the existing file to compare data with the API's
        :param json_file: file name
        :return: employees (data)
        """
        with open(json_file) as employees_file:
            employees = json.load(employees_file)
            return employees

    @staticmethod
    def extract_exc_employee_data():
        """
        Writes the excluded list of employees to file
        :return:
        """
        with open("exc_employees.json") as employees_file:
            exc_employees = json.load(employees_file)
            return exc_employees

    def write_wished_employees_to_json(self):
        """
        Writes the list of employees wished (emailed) birthday today
        :return:
        """
        with open(f'{self.__current_dir}/employees.json', 'w') as employees_file:
            json.dump(self.employees_list, employees_file)

    def write_not_celebrating_employees_to_json(self):
        """
        Writes the list of employees not wished (not emailed) birthday today.
        Basically the list of today's invalid employees
        :return:
        """
        with open(f'{self.__current_dir}/employees_na.json', 'w') as employees_not_today_file:
            json.dump(self.employees_na_list, employees_not_today_file)
