import requests
from os                                         import path

from core.anniversary                           import AnniversaryMessage
from core.birthday                              import BirthdayMessage
from db.data                                    import JSONData
from models.employee                            import Employee
from utils.process                              import ProcessEmployee


class GetInput:

    def __init__(self, selection):
        self.selection   = selection
        self.emp_list    = []
        self.emp_na_list = []
    
    def compare_api_and_local_data(self):
        for employee in self.employees_local:
            if self.worker['id'] == employee['id']:
                return True
        return False

    def call_real_endpoint(self):

        employees     = []
        exc_employees = []
        emp_resp      = requests.get('https://interview-assessment-1.realmdigital.co.za/employees')
        exc_emp_resp  = requests.get('https://interview-assessment-1.realmdigital.co.za/do-not-send-birthday-wishes')

        if emp_resp.status_code == 200:
            employees = emp_resp.json()
        if exc_emp_resp.status_code == 200:
            exc_employees = exc_emp_resp.json()

        data = {
            'employees'     : employees,
            'exc_employees' : exc_employees
        }

        return data

    def get_input_redirect(self):

        #TODO: TO REQUEST API ENDPOINT
        # data_api      = self.call_real_endpoint()
        # employees_api = data_api['employees']
        # employees     = employees_api

        self.employees_local = []
        if path.isfile('db/employeesZ.json'):
            data_local           = JSONData(None, None, None)
            self.employees_local = data_local.extract_employee_data()
            employees = self.employees_local

        # BIRTHDAY WISHES
        if self.selection == '1':
            for worker in employees:
                self.worker = worker

                # if self.compare_api_and_local_data():
                #     continue

                employee = Employee(self.worker, employees)
                is_valid = ProcessEmployee(employee).validate_employee_to_receive_msg()

                if is_valid:
                    BirthdayMessage(employee)
                    self.worker['lastNotification']     = employee.get_current_date.strftime('%Y-%m-%d')
                    self.worker['lastBirthdayNotified'] = employee.get_current_date.strftime('%Y-%m-%d')
                    self.emp_list.append(self.worker)
                else:
                    self.emp_na_list.append(self.worker)

            if self.emp_list:
                JSONData(self.emp_list, None, 'Y', self.emp_list, None).start()

            if self.emp_na_list:
                JSONData(None, self.emp_na_list, 'N', None, self.emp_na_list).start()

        # ANNIVERSARY WISHES
        if self.selection == '2':
            for worker in employees:
                self.worker = worker

                if self.compare_api_and_local_data():
                    continue

                employee = Employee(self.worker, employees)
                is_valid = ProcessEmployee(employee).validate_employee_to_receive_msg()

                if is_valid:
                    AnniversaryMessage(employee)
                    self.worker['lastNotification']     = employee.get_current_date.strftime('%Y-%m-%d')
                    self.worker['lastBirthdayNotified'] = employee.get_current_date.strftime('%Y-%m-%d')
                    self.emp_list.append(self.worker)
                else:
                    self.emp_na_list.append(self.worker)

            if self.emp_list:
                JSONData(self.emp_list, None, 'Y', self.emp_list, None).start()

            if self.emp_na_list:
                JSONData(None, self.emp_na_list, 'N', None, self.emp_na_list).start()

        return
