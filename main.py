import ttkbootstrap as ttk
from helpers import gui_creation, user_input_storage, database_connector
from helpers import job_number_storage, job_number_generator
from ttkbootstrap.constants import *

database_path = r"testing_helpers\TestDatabase.accdb"
input_storage = user_input_storage.UserInputStorage()
job_number_storage = job_number_storage.JobNumbers()
job_number_generator = job_number_generator.JobNumberGenerator(
    job_number_storage
)
access_database = database_connector.DatabaseConnection(database_path)

# Execute a SELECT query.
active_jobs = access_database.execute_query(
    "SELECT [Job Number] FROM [Existing Jobs] WHERE [Active] = Yes"
)

existing_jobs = access_database.execute_query(
    "SELECT [Job Number] FROM [Existing Jobs]"
)

job_number_storage.add_active_job_numbers(active_jobs)
job_number_storage.add_existing_job_numbers(existing_jobs)


def clear_gui(
    input_storage: user_input_storage.UserInputStorage = input_storage,
    white_listed_elements=[],
) -> None:
    for user_input in input_storage.input_objects.values():
        if user_input in white_listed_elements:
            continue
        elif isinstance(user_input, ttk.DateEntry):
            user_input.entry.delete(0, END)
        elif isinstance(user_input, ttk.Entry):
            user_input.delete(0, END)
        elif isinstance(user_input, ttk.Text):
            user_input.delete("1.0", "end-1c")


def submit_entry():
    access_database.insert_new_job("", input_storage.inputs)
    pass


def gather_database_fields():
    inputted_job_number = input_storage.input_objects["job_number"].get()
    clear_gui(
        white_listed_elements=[
            input_storage.input_objects["job_date"],
            input_storage.input_objects["fieldwork_date"],
            input_storage.input_objects["job_number"],
        ]
    )

    existing_job_numbers = job_number_storage.get_existing_job_numbers()

    if inputted_job_number in existing_job_numbers:
        existing_job_data = access_database.execute_query(
            f"SELECT * FROM [Existing Jobs]\
WHERE [Job Number] = '{inputted_job_number}'"
        )[0]
    else:
        return

    parcel_id = existing_job_data[2]
    entry_by = existing_job_data[9]
    requested_services = existing_job_data[13]
    contact_information = existing_job_data[11]
    additional_information = existing_job_data[12]
    input_storage.input_objects["parcel_id"].insert(0, parcel_id)
    input_storage.input_objects["entry_by"].insert(0, entry_by)
    input_storage.input_objects["requested_services"].insert(
        "1.0", requested_services
    )
    input_storage.input_objects["contact_info"].insert(
        "1.0", contact_information
    )
    input_storage.input_objects["additional_info"].insert(
        "1.0", additional_information
    )


def display_generated_job_number():
    existing_job_numbers = access_database.execute_query(
        "SELECT [Job Number] FROM [Existing Jobs]"
    )
    job_number_storage.clear_job_numbers()
    job_number_storage.add_existing_job_numbers(existing_job_numbers)
    job_number_storage.add_unused_job_number(
        job_number_generator.unused_job_number
    )
    unused_job_number = job_number_storage.unused_job_number
    input_storage.input_objects["job_number"].insert(0, unused_job_number)


def main() -> None:
    window_width = 500
    window_height = 555

    app = ttk.Window(
        maxsize=(window_width, window_height),
        minsize=(window_width, window_height),
    )

    user_input_objects = {}

    label = ttk.Label(app, text="Red Stake File Entry")
    label.pack(pady=10)
    label.config(font=("Arial", 20, "bold"))

    date_labels = {
        "Job Date": "job_date",
        "Fieldwork Date": "fieldwork_date",
    }

    single_line_labels = {
        "Job Number": "job_number",
        "Parcel ID": "parcel_id",
        "Entry By": "entry_by",
    }
    multi_line_labels = {
        "Requested Services": "requested_services",
        "Contact Information": "contact_info",
        "Additional Information": "additional_info",
    }

    buttons = {
        "Submit": submit_entry,
        "Generate FN": display_generated_job_number,
        "Gather Info": gather_database_fields,
        "Clear": clear_gui,
    }

    for label, name in date_labels.items():
        frame = gui_creation.create_frame(app)

        if label == "Job Date":
            bootstyle = PRIMARY
        else:
            bootstyle = SECONDARY

        user_input_objects[name] = gui_creation.create_date_entry(
            frame=frame, label_text=label, name=name, bootstyle=bootstyle
        )

    for label, name in single_line_labels.items():
        frame = gui_creation.create_frame(app)
        user_input_objects[name] = gui_creation.create_label_entry(
            frame=frame, label_text=label, name=name
        )

    for label, name in multi_line_labels.items():
        frame = gui_creation.create_frame(app)
        user_input_objects[name] = gui_creation.create_label_entry(
            frame=frame, label_text=label, name=name, multi_line=True
        )

    frame = gui_creation.create_frame(app)
    for button_label, button_function in buttons.items():
        gui_creation.create_button(
            frame=frame, text=button_label, command=button_function
        )

    input_storage.add_inputs(user_input_objects)
    input_storage.input_objects["job_number"].insert(0, "23030111")

    app.mainloop()


if __name__ == "__main__":
    main()
