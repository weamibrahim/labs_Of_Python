from employee import Employee
from DBHandler import DBHandler

from config import db_config


db = DBHandler(db_config).connect()


class Manager(Employee):

    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department
        db.update(
            f"update `employee` set managed_department =%s where first_name= %s and last_name = %s",
            (self.managed_department, self.first_name, self.last_name)
        )

    def show(self):
        print(f"first name is {self.first_name}")
        print(f"last name is {self.last_name}")
        print(f"age is  {self.age}")
        print(f"department is {self.department}")
        print(f"managed_department is {self.managed_department}")
        print(f"salary is ######")