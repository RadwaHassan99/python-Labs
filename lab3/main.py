from Classes.employee import Employee
from Classes.manager import Manager

MANAGER_TYPE = 'm'
EMPLOYEE_TYPE = 'e'

def display_employee_menu():
    print("Menu:")
    print("- To add a new employee, enter 'add'")
    print("- To transfer an employee to a new department, enter 'transfer'")
    print("- To fire an employee, enter 'fire'")
    print("- To list all employees, enter 'list'")
    print("- To show details of an employee, enter 'show'")
    print("- To exit the program, enter 'q'")
    print()
    print("If you're a manager, enter 'm'. If you're an employee, enter 'e'.")
    print()

def add_employee(EmployeeClass):
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = input("Age: ")
    department = input("Department: ")
    salary = input("Salary: ")
    managed_department = None
    if EmployeeClass == Manager:
        managed_department = input("Managed department: ")
    new_employee = EmployeeClass(first_name, last_name, age, department, salary, managed_department)

def transfer_employee(EmployeeClass):
    id = int(input("Employee ID: "))
    new_department = input("New department: ")
    EmployeeClass.transfer(id, new_department)

def fire_employee(EmployeeClass):
    id = int(input("Employee ID: "))
    EmployeeClass.fire(id)

def list_employees(EmployeeClass):
    EmployeeClass.list_employees()

def show_employee(EmployeeClass):
    id = int(input("Employee ID: "))
    print(id)
    EmployeeClass.show(id)

def run_employee_menu():
    while True:
        display_employee_menu()
        employee_type = input("Are you a manager or an employee? Enter 'm' or 'e': ")
        if employee_type not in (MANAGER_TYPE, EMPLOYEE_TYPE):
            print("Invalid input. Please try again.")
            continue
        
        if employee_type == MANAGER_TYPE:
            EmployeeClass = Manager
        else:
            EmployeeClass = Employee
        
        action = input("What would you like to do? ")
        if action == 'q':
            print("Exiting program...")
            break
        elif action == 'add':
            add_employee(EmployeeClass)
        elif action == 'transfer':
            transfer_employee(EmployeeClass)
        elif action == 'fire':
            fire_employee(EmployeeClass)
        elif action == 'list':
            list_employees(EmployeeClass)
        elif action == 'show':
            show_employee(EmployeeClass)
        else:
            print("Invalid input. Please try again.")


run_employee_menu()



