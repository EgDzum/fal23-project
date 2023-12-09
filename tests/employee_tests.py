from unittest import TestCase


class EmployeeTests(TestCase):

    def test_create_employee_instance_ideal(self):
        empl_obj = Employee(
            name='test',
            surname='test',
            age=100,
            salary=Salary(
                amount=10000,
                currency=CURRENCIES.RUBLE
            )
        )
        self.assertTrue(empl_obj)