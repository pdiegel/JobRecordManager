import ttkbootstrap as ttk
from helpers import gui_creation
from ttkbootstrap.constants import *

user_input_objects = []


def clear_gui():
    for user_input in user_input_objects:
        if isinstance(user_input, ttk.DateEntry):
            user_input.entry.delete(0, END)
        elif isinstance(user_input, ttk.Entry):
            user_input.delete(0, END)
        elif isinstance(user_input, ttk.Text):
            user_input.delete("1.0", "end-1c")


def submit_entry():
    pass


def generate_fn():
    pass


def gather_database_fields():
    pass


def gather_inputs():
    user_inputs = []

    for user_input in user_input_objects:
        if isinstance(user_input, ttk.DateEntry):
            user_inputs.append(user_input.entry.get())
        elif isinstance(user_input, ttk.Entry):
            user_inputs.append(user_input.get())
        elif isinstance(user_input, ttk.Text):
            user_inputs.append(user_input.get("1.0", "end-1c"))

    return user_inputs


def main() -> None:
    window_width = 500
    window_height = 555

    app = ttk.Window(
        maxsize=(window_width, window_height),
        minsize=(window_width, window_height),
    )

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
        "Generate FN": generate_fn,
        "Gather Info": gather_inputs,
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

    app.mainloop()


if __name__ == "__main__":
    main()
