import pyodbc


class DatabaseConnection:
    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connect()

    def connect(self):
        connection_str = (
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={self.database_path};"
        )
        self.connection = pyodbc.connect(connection_str)

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query: str, parameters: tuple = None):
        with self.connection.cursor() as cursor:
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def execute_non_query(self, query: str, parameters: tuple = None):
        with self.connection.cursor() as cursor:
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            self.connection.commit()


"""
from helpers.database_connection import DatabaseConnection

# Replace this with the path to your Access database file.
database_path = 'path/to/your/access/database.accdb'

db_connection = DatabaseConnection(database_path)
db_connection.connect()

# Execute a SELECT query.
query_result = db_connection.execute_query('SELECT * FROM your_table_name')
print(query_result)

# Execute an INSERT, UPDATE or DELETE query.
db_connection.execute_non_query('UPDATE your_table_name SET column_name = ?
WHERE id = ?', (new_value, record_id))

db_connection.close()
"""
