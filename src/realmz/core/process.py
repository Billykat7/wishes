class ProcessEmployee:
    """
    Processes the employees to receive the message
    """

    def __init__(self, employee):
        self.employee = employee

    def validate_birthdays_employees(self):
        """
        Validates birthday employees
        :return: boolean
        """

        if self.employee.get_last_birthday_notification != self.employee.get_current_date:
            if self.employee.has_started_working:
                if self.employee.is_still_working:
                    if self.employee.can_receive_wishes:
                        if self.employee.is_today_birthday_celebration:
                            return True
        return False

    def validate_anniversary_employees(self):
        """
        Validates anniversary employees
        :return: boolean
        """

        if self.employee.get_last_notification != self.employee.get_current_date:
            if self.employee.has_started_working:
                if self.employee.is_still_working:
                    if self.employee.can_receive_wishes:
                        if self.employee.is_today_anniversary_celebration:
                            return True
        return False
