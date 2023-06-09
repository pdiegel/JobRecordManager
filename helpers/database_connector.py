"""This module contains the DatabaseConnection class."""
import pyodbc
from parcel_data_collector.county_property_data import ParcelDataCollection

from config import ACTIVE_DB_COLUMN_ORDER, EXISTING_DB_COLUMN_ORDER


class DatabaseConnection:
    """This class is used to manage the database connection and execute
    queries."""

    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = self.connect()

    def connect(self) -> None:
        """Connects to the Microsoft Access database."""
        connection_str = (
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={self.database_path};"
        )
        return pyodbc.connect(connection_str)

    def close(self) -> None:
        """Closes the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query: str, parameters: tuple = None) -> [tuple]:
        """Executes a query and returns the results."""
        with self.connection.cursor() as cursor:
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def execute_non_query(self, query: str, parameters: tuple = None) -> None:
        """Executes a query that does not return any results."""
        with self.connection.cursor() as cursor:
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            self.connection.commit()

    def insert_new_job(self, user_inputs: dict) -> None:
        """Inserts a new job into the database."""
        parcel = ParcelDataCollection(user_inputs["parcel_id"])
        parcel_data = parcel.parcel_data
        parcel_data["county"] = parcel.county

        self.merge_user_inputs_into_parcel_data(user_inputs, parcel_data)

        try:
            self.create_new_job(parcel_data)
        except pyodbc.IntegrityError as error:
            print(error)
            self.update_existing_job(parcel_data)

        try:
            self.add_to_active_jobs(parcel_data)
        except pyodbc.IntegrityError as error:
            print(error)

        self.connection.commit()

    def update_existing_job(self, parcel_data: dict) -> None:
        """Updates an existing job in the database."""
        sql_query = self.create_update_query(parcel_data)
        self.execute_non_query(sql_query)

    def merge_user_inputs_into_parcel_data(
        self, user_inputs: dict, parcel_data: dict
    ) -> None:
        """Merges the user inputs into the parcel data dictionary."""
        database_columns = set(
            EXISTING_DB_COLUMN_ORDER + ACTIVE_DB_COLUMN_ORDER
        )

        for column in database_columns:
            if column in user_inputs and column not in parcel_data:
                parcel_data[column] = user_inputs[column]
            elif column not in parcel_data:
                parcel_data[column] = None

    def create_new_job(
        self,
        parcel_data: dict,
    ) -> None:
        """Creates a new job in the database."""
        self.execute_non_query(
            "INSERT INTO [Existing Jobs]\
 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            [parcel_data[column] for column in EXISTING_DB_COLUMN_ORDER],
        )

    def create_update_query(self, parcel_data: dict) -> str:
        """Creates and returns an SQL query to update the database
        with new data."""

        sql_query = f"""
            UPDATE [Existing Jobs]
            SET [Job Date] = '{parcel_data["job_date"]}',
                [Parcel ID] = '{parcel_data["parcel_id"]}',
                [subdivision] = '{parcel_data["subdivision"]}',
                [Lot] = '{parcel_data["lot"]}',
                [block] = '{parcel_data["block"]}',
                [Plat Book] = '{parcel_data["plat_book"]}',
                [Plat Page] = '{parcel_data["plat_page"]}',
                [Legal Description] = '{parcel_data["legal_description"]}',
                [Entry By] = '{parcel_data["entry_by"]}',
                [Additional Information] = '{parcel_data["additional_info"]}',
                [Customer Contact Information] = '{
                    parcel_data["contact_info"]}'
            WHERE [Job Number] = '{parcel_data["job_number"]}'
            """
        return sql_query

    def add_to_active_jobs(self, parcel_data: dict) -> str:
        """Creates and returns an SQL query to update the database
        with new data."""

        self.execute_non_query(
            "INSERT INTO [Active Jobs]\
 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            [parcel_data[column] for column in ACTIVE_DB_COLUMN_ORDER],
        )
