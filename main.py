from functools import partial

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from config import *
from helpers import gui_creation as gui
from helpers.controller import Controller


def create_input_fields(app: ttk.Window, controller: Controller) -> None:
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
        "Inhouse Status": "inhouse_status",
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

    controller.input_storage.add_inputs(date_input_objects)
    controller.input_storage.add_inputs(single_line_input_objects)
    controller.input_storage.add_inputs(multi_line_input_objects)


def create_buttons_and_commands(
    app: ttk.Window, controller: Controller
) -> None:
    """
    Creates buttons and assigns their commands.
    """
    buttons_and_commands = {
        "Submit": controller.submit_user_input,
        "Generate FN": controller.update_job_number_display,
        "Gather Info": controller.retrieve_existing_job_data,
        "Clear": controller.clear_input_fields,
    }

    gui.create_buttons(app, buttons_and_commands)


def configure_main_window(app: ttk.Window) -> None:
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
    inputs, and buttons. The inputs are stored in the Controller's
    UserInputStorage object for further processing.
    """

    controller = Controller()

    app = ttk.Window(
        maxsize=(WINDOW_WIDTH, WINDOW_HEIGHT),
        minsize=(WINDOW_WIDTH, WINDOW_HEIGHT),
    )

    configure_main_window(app)
    create_input_fields(app, controller)
    create_buttons_and_commands(app, controller)

    # For manual testing purposes.
    controller.input_storage.input_objects["job_number"].insert(0, "23030160")

    app.mainloop()


def main() -> None:
    initialize_app()


if __name__ == "__main__":
    main()
