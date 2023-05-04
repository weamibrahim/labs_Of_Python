from DBHandler import DBHandler
from config import db_config

db =DBHandler(db_config).connect()
class Employee:
   employees=[]  
   def __init__(self, first_name,last_name,age,department,salary):
      self.first_name=first_name
      self.last_name =last_name
      self.age=age
      self.department=department
      self.salary=salary  
      Employee.employees.append(self)
      db.insert(
         f"insert into `employee` (`first_name`,`last_name`,`age`,`department`,`salary`) VALUES (%s, %s, %s, %s, %s)",
         (self.first_name, self.last_name,
         self.age, self.department, self.salary)
      ) 
   
   def transfer(self,department):
      self.department = department
      db.update(f"update `employee` set department =%s where first_name= %s and last_name = %s",(self.department, self.first_name, self.last_name))
   
   def fire(self):
      Employee.employees.remove(self)
      db.remove(f"delete from `employee` where first_name= %s and last_name = %s",
      (self.first_name, self.last_name))

   def show(self):
      print(f"first name is {self.first_name}")
      print(f"last name is {self.last_name}")
      print(f"age is {self.age}")
      print(f"department is {self.department}")
      print(f"salary is {self.salary}")

   @staticmethod
   def list_employees():
      employees = db.fetch_all(
         query=f"select * from `employee` where `managed_department` is Null"
      )
      for emp in employees:
        print(f"first name is {emp[0]}")
        print(f"last name is {emp[1]}")
        print(f"salary is {emp[2]}")
        print(f"age is {emp[3]}")
        print(f"department is {emp[4]}")
      




