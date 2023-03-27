from functools import partial

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from config import *
from helpers import database_connector
from helpers import gui_creation as gui
from helpers import (
    job_number_generator,
    job_number_storage,
    user_input_storage,
)


def clear_input_fields(
    input_storage: user_input_storage.UserInputStorage,
    excluded_elements=[],
) -> None:
    """
    Clears the input fields in the GUI by resetting their values to
    empty strings or default values.

    Args:
        input_storage (user_input_storage.UserInputStorage, optional):
            A UserInputStorage object containing the input objects
            (widgets) to be cleared. Defaults to input_storage.

        excluded_elements (List[Union[ttk.DateEntry, ttk.Entry,
            ttk.Text]], optional): A list of input objects (widgets)
            that should be excluded from the clearing process. Defaults
            to an empty list.
    """
    for user_input in input_storage.input_objects.values():
        if user_input in excluded_elements:
            continue
        elif isinstance(user_input, ttk.DateEntry):
            user_input.entry.delete(0, END)
        elif isinstance(user_input, ttk.Entry):
            user_input.delete(0, END)
        elif isinstance(user_input, ttk.Text):
            user_input.delete("1.0", "end-1c")


def update_input_value(input_object, data) -> None:
    """
    Updates the value of a given input object (widget) with the provided
    data.

    Args:
        input_object (Union[ttk.Entry, ttk.Text]): The input object
            (widget) whose value will be updated.

        data (Any): The data to be inserted into the input object.

    Note:
        This function supports ttk.Entry and ttk.Text input objects.
    """
    if isinstance(input_object, ttk.Entry):
        input_object.delete(0, END)
        input_object.insert(0, data)
    elif isinstance(input_object, ttk.Text):
        input_object.delete("1.0", "end-1c")
        input_object.insert("1.0", data)


def submit_user_input(
    access_database: database_connector.DatabaseConnection,
) -> None:
    """
    Submits the user input to the database by calling the
    'insert_new_job' method.

    Args:
        access_database (database_connector.DatabaseConnection):
            An instance of the DatabaseConnection class.

    Note:
        The 'insert_new_job' method is responsible for adding the user
        input to the database.
    """
    access_database.insert_new_job(input_storage.inputs)


def retrieve_existing_job_data(
    input_storage: user_input_storage.UserInputStorage,
    job_numbers: job_number_storage.JobNumbers,
    access_database: database_connector.DatabaseConnection,
) -> None:
    """
    Retrieves existing job data from the database based on the inputted
    job number and updates the corresponding input fields in the user
    interface.

    Args:
        input_storage (user_input_storage.UserInputStorage): An instance
            of UserInputStorage class.

        job_numbers (job_number_storage.JobNumbers): An instance of
            JobNumbers class.

        access_database (database_connector.DatabaseConnection):
            An instance of DatabaseConnection class.
    """
    inputted_job_number = input_storage.input_objects["job_number"].get()
    clear_input_fields(
        input_storage,
        excluded_elements=[
            input_storage.input_objects["job_date"],
            input_storage.input_objects["fieldwork_date"],
            input_storage.input_objects["job_number"],
        ],
    )

    existing_job_numbers = job_numbers.get_existing_job_numbers()

    if inputted_job_number in existing_job_numbers:
        existing_job_data = access_database.execute_query(
            f"SELECT * FROM [Existing Jobs]\
 WHERE [Job Number] = '{inputted_job_number}'"
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
            update_input_value(input_storage.input_objects[field], data)


def update_job_number_display(
    job_numbers: job_number_storage.JobNumbers,
    generator: job_number_generator.JobNumberGenerator,
    access_database: database_connector.DatabaseConnection,
    input_storage: user_input_storage.UserInputStorage,
) -> None:
    """
    Updates the job number input field with the next unused job number,
    generated based on the current year and existing job numbers in the
    database.

    Args:
        job_numbers (job_number_storage.JobNumbers):
            An instance of JobNumbers class.

        generator (job_number_generator.JobNumberGenerator):
            An instance of JobNumberGenerator class.

        access_database (database_connector.DatabaseConnection):
            An instance of DatabaseConnection class.
    """
    current_year = generator.year
    existing_current_year_jobs = access_database.execute_query(
        f"SELECT [Job Number] FROM [Existing Jobs] WHERE [Job Number]\
 LIKE '{current_year}%'"
    )
    job_numbers.add_current_year_job_numbers(existing_current_year_jobs)
    job_numbers.add_unused_job_number(generator.unused_job_number)
    unused_job_number = job_numbers.unused_job_number

    input_storage.input_objects["job_number"].delete(0, END)
    input_storage.input_objects["job_number"].insert(0, unused_job_number)


def create_input_fields(
    app: ttk.Window, input_storage: user_input_storage.UserInputStorage
) -> None:
    """
    Creates input fields and stores them in the input_storage object.
    """
    date_input_labels = {
        "Job Date": "job_date",
        "Fieldwork Date": "fieldwork_date",
    }

    single_line_input_labels = {
        "Job Number": "job_number",
        "Parcel ID": "parcel_id",
        "Entry By": "entry_by",
    }
    multi_line_input_labels = {
        "Requested Services": "requested_services",
        "Contact Information": "contact_info",
        "Additional Information": "additional_info",
    }

    date_input_objects = gui.create_date_entries(app, date_input_labels)
    single_line_input_objects = gui.create_single_line_entries(
        app, single_line_input_labels
    )
    multi_line_input_objects = gui.create_multi_line_entries(
        app, multi_line_input_labels
    )

    input_storage.add_inputs(date_input_objects)
    input_storage.add_inputs(single_line_input_objects)
    input_storage.add_inputs(multi_line_input_objects)


def create_buttons_and_commands(
    app: ttk.Window,
    input_storage: user_input_storage.UserInputStorage,
    job_numbers: job_number_storage.JobNumbers,
    generator: job_number_generator.JobNumberGenerator,
    access_database: database_connector.DatabaseConnection,
) -> None:
    """
    Creates buttons and assigns their commands.
    """
    buttons_and_commands = {
        "Submit": partial(submit_user_input, access_database=access_database),
        "Generate FN": partial(
            update_job_number_display,
            job_numbers=job_numbers,
            generator=generator,
            access_database=access_database,
            input_storage=input_storage,
        ),
        "Gather Info": partial(
            retrieve_existing_job_data,
            input_storage=input_storage,
            job_numbers=job_numbers,
            access_database=access_database,
        ),
        "Clear": partial(clear_input_fields, input_storage=input_storage),
    }

    gui.create_buttons(app, buttons_and_commands)


def configure_main_window(app) -> None:
    """
    Configures the main application window.
    """
    label = ttk.Label(app, text="Red Stake File Entry")
    label.pack(pady=10)
    label.config(font=("Arial", 20, "bold"))


def initialize_app() -> None:
    """
    Initializes the main application window, creates input fields and
    buttons, and starts the Tkinter main loop.

    This function sets up the Tkinter window with the desired layout and
    widgets. It creates date inputs, single-line inputs, multi-line
    inputs, and buttons. The inputs are stored in the UserInputStorage
    object for further processing.
    """

    input_storage = user_input_storage.UserInputStorage()
    job_numbers = job_number_storage.JobNumbers()
    job_num_generator = job_number_generator.JobNumberGenerator(job_numbers)
    access_database = database_connector.DatabaseConnection(DATABASE_PATH)

    active_jobs = access_database.execute_query(
        "SELECT [Job Number] FROM [Active Jobs]"
    )

    existing_jobs = access_database.execute_query(
        "SELECT [Job Number] FROM [Existing Jobs]"
    )

    job_numbers.add_active_job_numbers(active_jobs)
    job_numbers.add_existing_job_numbers(existing_jobs)

    app = ttk.Window(
        maxsize=(WINDOW_WIDTH, WINDOW_HEIGHT),
        minsize=(WINDOW_WIDTH, WINDOW_HEIGHT),
    )

    configure_main_window(app)
    create_input_fields(app, input_storage)
    create_buttons_and_commands(
        app, input_storage, job_numbers, job_num_generator, access_database
    )

    # For manual testing purposes.
    input_storage.input_objects["job_number"].insert(0, "23030160")

    app.mainloop()


def main() -> None:
    initialize_app()


if __name__ == "__main__":
    main()
