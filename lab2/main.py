from employee import Employee

from manager import Manager
def main():
  while True: #make the code run except the user wants to exit 
        print("Select an operation:")
        print(" Enter (e) to Add new employee")
        print(" Enter (m) to Add new manager")
        print(" Enter (t) to Transfer employee")
        print(" Enter (s) to Show employee/manager")
        print(" Enter (l) to List all employees/managers")
        print(" Enter (f) to Fire employee/manager")
        print(" Enter (q) to Quit")
        
        operation = input("Enter the operation you want: ")

        if operation == 'e':
             addEmployee()
        elif operation == 'm':
             addManager()
        elif operation == 't':
            transferEmployee()
        elif operation == 's':
            showEmployee()
        elif operation == 'l':
            listEmployees()
        elif operation == 'f':
            fireEmployee()
        elif operation == 'q':
            break
        else:
            print("Invalid operation")
            
            def addEmployee():
             print("Adding new employee:")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            age = int(input("Age: "))
            dept = input("Department: ")
            salary = int(input("Salary: "))
            Employee(first_name, last_name, age, dept, salary)
            print("Employee added successfully")

#make an instance of manager class  
def addManager():
    print("Adding new manager:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    dept = input("Department: ")
    salary = float(input("Salary: "))
    managed_department = input("Managed department: ")
    Manager(first_name, last_name, age, dept, salary, managed_department)
    print("Manager added successfully")


def transferEmployee():
    id = int(input("Enter employee/manager ID: "))
    dept = input("Enter new department: ")
    emp = findEmployee(id)
    if emp:
        emp.transfer(dept)
        print("Employee/manager transferred successfully")
    else:
        print("Employee/manager not found")

def showEmployee():
    id = int(input("Enter employee/manager ID: "))
    emp = findEmployee(id)
    if emp:
        emp.show()
    else:
        print("Employee/manager not found")

def listEmployees():
    print("All employees/managers:")
    Employee.listEmployees()

def fireEmployee():
    id = int(input("Enter employee/manager ID: "))
    emp = findEmployee(id)
    if emp:
        emp.fire()
        print("Employee/manager fired successfully")
    else:
        print("Employee/manager not found")

#find the employee/manager in the list 
def findEmployee(id):
    for emp in Employee.all_employees:
        if emp._id == id:
            return emp
    return None

if __name__ == '__main__':
    main()
   