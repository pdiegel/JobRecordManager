import ttkbootstrap as ttk
from helpers import gui_creation, user_input_storage, database_connector
from helpers import job_number_storage, job_number_generator
from ttkbootstrap.constants import *

database_path = r"\\Server\access\Database Backup\MainDB_be.accdb"
input_storage = user_input_storage.UserInputStorage()
job_number_storage = job_number_storage.JobNumbers()
job_number_generator = job_number_generator.JobNumberGenerator(
    job_number_storage
)
access_database = database_connector.DatabaseConnection(database_path)

# Execute a SELECT query.
existing_jobs = access_database.execute_query(
    "SELECT [Job Number] FROM [Existing Jobs]"
)

active_jobs = access_database.execute_query(
    "SELECT [Job Number] FROM [Active Jobs]"
)

job_number_storage.add_existing_job_numbers(existing_jobs)
job_number_storage.add_active_job_numbers(active_jobs)
job_number_storage.add_unused_job_number(
    job_number_generator.unused_job_number
)
# print(job_number_storage.get_existing_job_numbers())
# print(job_number_storage.get_active_job_numbers())

print(job_number_storage.unused_job_number)


def clear_gui(
    input_storage: user_input_storage.UserInputStorage = input_storage,
) -> None:
    print(input_storage.inputs)
    for user_input in input_storage.input_objects:
        if isinstance(user_input, ttk.DateEntry):
            user_input.entry.delete(0, END)
        elif isinstance(user_input, ttk.Entry):
            user_input.delete(0, END)
        elif isinstance(user_input, ttk.Text):
            user_input.delete("1.0", "end-1c")


def submit_entry():
    pass


def gather_database_fields():
    pass


def main() -> None:
    window_width = 500
    window_height = 555

    app = ttk.Window(
        maxsize=(window_width, window_height),
        minsize=(window_width, window_height),
    )

    user_input_objects = []

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
        "Generate FN": print,
        "Gather Info": gather_database_fields,
        "Clear": clear_gui,
    }

    for label, name in date_labels.items():
        frame = gui_creation.create_frame(app)

        if label == "Job Date":
            bootstyle = PRIMARY
        else:
            bootstyle = SECONDARY

        user_input_objects.append(
            gui_creation.create_date_entry(
                frame=frame, label_text=label, name=name, bootstyle=bootstyle
            )
        )

    for label, name in single_line_labels.items():
        frame = gui_creation.create_frame(app)
        user_input_objects.append(
            gui_creation.create_label_entry(
                frame=frame, label_text=label, name=name
            )
        )

    for label, name in multi_line_labels.items():
        frame = gui_creation.create_frame(app)
        user_input_objects.append(
            gui_creation.create_label_entry(
                frame=frame, label_text=label, name=name, multi_line=True
            )
        )

    frame = gui_creation.create_frame(app)
    for button_label, button_function in buttons.items():
        gui_creation.create_button(
            frame=frame, text=button_label, command=button_function
        )

    input_storage.add_inputs(user_input_objects)

    app.mainloop()


if __name__ == "__main__":
    main()
