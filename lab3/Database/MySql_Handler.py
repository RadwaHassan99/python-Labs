import mysql.connector
from mysql.connector import Error


class MySqlHandler:
    def __init__(self, table):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '12345'
        self.database = 'python_lab2'
        self.table = table
        self.connection = None

    def connect_to_DB(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
                )
            print("Connected to MySQL database")
        except Error as e:
            print("Error connecting to MySQL database: ", e)

    def disconnect_DB(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL database connection closed")

    def insert_record(self, data):
        self.connect_to_DB()
        cols = ', '.join(data.keys())
        vals = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.table} ({cols}) VALUES ({vals})"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            employee_id = cursor.lastrowid
            print(f"{cursor.rowcount} record(s) inserted successfully")
        except Error as e:
            print("Error inserting record: ", e)
        finally:
            self.disconnect_DB()
            return employee_id

    def update_record(self, id, data):
        self.connect_to_DB()
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {self.table} SET {set_clause} WHERE id = %s"
        values = list(data.values())
        values.append(id)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, tuple(values))
            self.connection.commit()
            print(f"{cursor.rowcount} record(s) updated successfully")
        except Error as e:
            print("Error updating record: ", e)
        finally:
            self.disconnect_DB()

    def delete_record(self, id):
        self.connect_to_DB()
        query = f"DELETE FROM {self.table} WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            self.connection.commit()
            print(f"{cursor.rowcount} record(s) deleted successfully")
        except Error as e:
            print("Error deleting record: ", e)
        finally:
            self.disconnect_DB()

    def get_all_records(self):
        self.connect_to_DB()
        query = f"SELECT * FROM {self.table}"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            print(f"{cursor.rowcount} record(s) retrieved successfully")
            return result
        except Error as e:
            print("Error retrieving records: ", e)
        finally:
            self.disconnect_DB()

    def get_record_by_id(self, id):
        self.connect_to_DB()
        query = f"SELECT * FROM {self.table} WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            print(f"{cursor.rowcount} record(s) retrieved successfully")
            return result
        except Error as e:
            print("Error retrieving record: ", e)
        finally:
            self.disconnect_DB()

















                      





 



