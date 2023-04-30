from Classes.employee import Employee
from prettytable import PrettyTable

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        self.managed_department = managed_department
        super().__init__(first_name, last_name, age, department, salary,managed_department)

    @classmethod
    def show(cls, id):
        for row in cls.employees:
            if row[0] == id:
                if (row[6]!=' '):
                    record = cls.DBhandler.get_record_by_id(id)
                    cls.print_data(record)
                else:
                    print("Error: Show can only be called on Manager objects")
                break
        else:
            print(f"No employee with ID {id} found")

    @staticmethod
    def print_data(record):
        table = PrettyTable()
        table.field_names = ["ID", "First Name", "Last Name", "Age", "Department", "Salary","Mangaed_department"]
        table.add_row([record[0], record[1], record[2], record[3], record[4],'Confidential',record[6]])
        print(table)

  
