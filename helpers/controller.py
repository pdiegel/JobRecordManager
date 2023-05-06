"""This module contains the Controller class.
The Controller class is used to manage the application's data and user
input. It is responsible for updating the GUI and the database."""

import ttkbootstrap as ttk
from ttkbootstrap.constants import END

from config import DATABASE_PATH
from helpers.database_connector import DatabaseConnection
from helpers.job_number_generator import JobNumberGenerator
from helpers.job_number_storage import JobNumbers
from helpers.user_input_storage import UserInputStorage


class Controller:
    """This class is used to manage the application's data and user
    input."""

    def __init__(self):
        self.input_storage = UserInputStorage()
        self.job_storage = JobNumbers()
        self.job_generator = JobNumberGenerator(self.job_storage)
        self.database = DatabaseConnection(DATABASE_PATH)

        active_jobs = self.database.execute_query(
            "SELECT [Job Number] FROM [Active Jobs]"
        )

        existing_jobs = self.database.execute_query(
            "SELECT [Job Number] FROM [Existing Jobs]"
        )

        self.job_storage.add_active_job_numbers(active_jobs)
        self.job_storage.add_existing_job_numbers(existing_jobs)

    def clear_input_fields(self, excluded_elements=[]) -> None:
        """
        Clears the input fields in the GUI by resetting their values to
        empty strings or default values.
        """
        for user_input in self.input_storage.input_objects.values():
            if user_input in excluded_elements:
                continue
            elif isinstance(user_input, ttk.DateEntry):
                user_input.entry.delete(0, END)
            elif isinstance(user_input, ttk.Entry):
                user_input.delete(0, END)
            elif isinstance(user_input, ttk.Text):
                user_input.delete("1.0", "end-1c")

    def update_input_value(self, input_object, data) -> None:
        """
        Updates the value of a given input object (widget) with the provided
        data.
        """
        if isinstance(input_object, ttk.Entry):
            input_object.delete(0, END)
            input_object.insert(0, data)
        elif isinstance(input_object, ttk.Text):
            input_object.delete("1.0", "end-1c")
            input_object.insert("1.0", data)

    def submit_user_input(self) -> None:
        """
        Submits the user input to the database by calling the
        'insert_new_job' method.

        Note:
            The 'insert_new_job' method is responsible for adding the user
            input to the database.
        """
        self.database.insert_new_job(self.input_storage.inputs)

    def retrieve_existing_job_data(self) -> None:
        """
        Retrieves existing job data from the database based on the inputted
        job number and updates the corresponding input fields in the user
        interface.
        """
        input_objects = self.input_storage.input_objects
        job_number = input_objects["job_number"].get()
        self.clear_input_fields(
            excluded_elements=[
                input_objects["job_date"],
                input_objects["fieldwork_date"],
                input_objects["job_number"],
            ]
        )

        existing_job_numbers = self.job_storage.get_existing_job_numbers()

        if job_number in existing_job_numbers:
            existing_job_data = self.database.execute_query(
                f"SELECT * FROM [Existing Jobs]\
    WHERE [Job Number] = '{job_number}'"
            )[0]
        else:
            return

        field_mapping = {
            "parcel_id": existing_job_data[4],
            "entry_by": existing_job_data[11],
            "contact_info": existing_job_data[13],
            "additional_info": existing_job_data[12],
        }

        for field, data in field_mapping.items():
            if data:
                self.update_input_value(input_objects[field], data)

    def update_job_number_display(self) -> None:
        """
        Updates the job number input field with the next unused job number,
        generated based on the current year and existing job numbers in the
        database.
        """
        input_objects = self.input_storage.input_objects
        current_year = self.job_generator.year

        existing_current_year_jobs = self.database.execute_query(
            f"SELECT [Job Number] FROM [Existing Jobs] WHERE [Job Number]\
    LIKE '{current_year}%'"
        )
        self.job_storage.add_current_year_job_numbers(
            existing_current_year_jobs
        )
        self.job_storage.add_unused_job_number(
            self.job_generator.unused_job_number
        )
        unused_job_number = self.job_storage.unused_job_number

        input_objects["job_number"].delete(0, END)
        input_objects["job_number"].insert(0, unused_job_number)
