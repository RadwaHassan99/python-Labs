from Database.MySql_Handler import MySqlHandler
from prettytable import PrettyTable

class Employee:

    db_table = 'employees'
    DBhandler = MySqlHandler(db_table) 
    employees = [list(row) for row in DBhandler.get_all_records()]

    def __init__(self,first_name, last_name, age, department, salary,managed_department=' '):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.db_handler = self.__class__.DBhandler
        self.id= self.insert()
        self.managed_department = managed_department
        self.__class__.employees.append([self.id, self.first_name, self.last_name, self.age, self.department, self.salary, self.managed_department])
        print(self.__class__.employees)  
    
    def insert(self):
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'department': self.department,
            'salary': self.salary,
            'managed_department':self.managed_department
            }
        return self.db_handler.insert_record(data)
    
    @classmethod
    def transfer(cls, id, new_department):
        if cls.is_valid_id(id):
            for employee in cls.employees:
                if employee[0] == id:
                    employee[4] = new_department
                    data = {'department': new_department}
                    cls.DBhandler.update_record(id, data)
        else:
            print(f"Invalid id: {id}")

    @classmethod
    def fire(cls, id):
        if cls.is_valid_id(id):
            cls.DBhandler.delete_record(id)
            cls.employees = [employee for employee in cls.employees if employee[0] != id]
        else:
            print(f"Invalid id: {id}")

    @classmethod
    def list_employees(cls):
        for employee in cls.employees:
            cls.print_data(employee)

    @classmethod
    def show(cls, id):
        if cls.is_valid_id(id):
            for row in cls.employees:
                if row[0] == id:
                    cls.print_data(row)
        else:
            print(f"Invalid id: {id}")

    @classmethod
    def is_valid_id(cls, id):
        for employee in cls.employees:
            if employee[0] == id:
                return True
        return False

    @classmethod
    def print_data(cls, employee):
        table = PrettyTable()
        table.field_names = ["ID", "First Name", "Last Name", "Age", "Department", "Salary","managed_department"]
        if(employee[6]!=' '):
            table.add_row([employee[0], employee[1], employee[2], employee[3], employee[4],'Confidential',employee[6]])
        else:
            table.add_row([employee[0], employee[1], employee[2], employee[3], employee[4],employee[5],employee[6]])
        print(table)


