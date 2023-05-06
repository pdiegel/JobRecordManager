"""This module contains functions for creating GUI elements."""

from typing import Tuple, Union

import ttkbootstrap as ttk
from ttkbootstrap.constants import LEFT, RIGHT, X

# Define a type alias for a widget font
WidgetFont = Tuple[str, int]


def create_label_entry(
    frame: ttk.Frame,
    label_text: str,
    name: str,
    label_font: WidgetFont = ("Arial", 14),
    entry_font: WidgetFont = ("Arial", 12),
    multi_line: bool = False,
) -> Union[ttk.Entry, ttk.Text]:
    """
    Creates a label and an entry (single-line or multi-line) in the
    given frame.

    Args:
        frame (ttk.Frame): The frame to place the label and entry
            widgets.
        label_text (str): The text for the label.
        name (str): The name of the entry widget.
        label_font (WidgetFont, optional):
            The font for the label. Defaults to ("Arial", 14).
        entry_font (WidgetFont, optional):
            The font for the entry. Defaults to ("Arial", 12).
        multi_line (bool, optional):
            Whether to create a multi-line entry. Defaults to False.

    Returns:
        Union[ttk.Entry, ttk.Text]: The created entry widget.
    """
    create_label(frame, label_text, label_font)

    if multi_line:
        entry = create_multi_line_entry(frame, entry_font, name)
    else:
        entry = create_single_line_entry(frame, entry_font, name)
    return entry


def create_date_entry(
    frame: ttk.Frame,
    label_text: str,
    name: str,
    label_font: WidgetFont = ("Arial", 14),
    bootstyle: str = "primary",
    padx: int = 5,
    pady: int = 3,
    fill: str = X,
) -> ttk.DateEntry:
    """
    Creates a label and a date entry in the given frame.

    Args:
        frame (ttk.Frame):
            The frame to place the label and date entry widgets.
        label_text (str): The text for the label.
        name (str): The name of the date entry widget.
        label_font (WidgetFont, optional):
            The font for the label. Defaults to ("Arial", 14).
        bootstyle (str, optional):
            The bootstrap style for the date entry. Defaults to
            "primary".
        padx (int, optional):
            The horizontal padding for the date entry. Defaults to 5.
        pady (int, optional):
            The vertical padding for the date entry. Defaults to 3.
        fill (str, optional):
            The fill option for the date entry's pack method. Defaults
            to X.

    Returns:
        ttk.DateEntry: The created date entry widget.
    """
    create_label(frame, label_text, label_font)

    date_entry = ttk.DateEntry(frame, bootstyle=bootstyle, name=name)
    date_entry.pack(pady=pady, padx=padx, fill=fill)
    return date_entry


def create_label(
    frame: ttk.Frame,
    text: str,
    font: WidgetFont,
    side: str = LEFT,
    padx: int = 5,
    pady: int = 3,
) -> ttk.Label:
    """
    Create a label widget and add it to a frame.

    Args:
        frame (ttk.Frame):
            The frame to place the label and date entry widgets.
        text (str): The text for the label.
        font (WidgetFont, optional):
            The font for the label. Defaults to ("Arial", 14).
        side (str, optional): The side of the frame on which to place
            the label. Defaults to LEFT.
        padx (int, optional):
            The horizontal padding for the date entry. Defaults to 5.
        pady (int, optional):
            The vertical padding for the date entry. Defaults to 3.

    Returns:
        The ttk.Label widget that was created.
    """
    label = ttk.Label(frame, text=text)
    label.pack(side=side, padx=padx, pady=pady)
    label.config(font=font)
    return label


def create_frame(
    window: ttk.Window, padx: int = 10, pady: int = 5, fill: str = X
) -> ttk.Frame:
    """
    Create a frame widget and add it to a window.

    Args:
        window (ttk.Window): The ttk.Window to which the frame should be
            added.
        padx (int, optional):
            The horizontal padding for the date entry. Defaults to 10.
        pady (int, optional):
            The vertical padding for the date entry. Defaults to 5.
        fill (str, optional): The fill mode to use for the frame.
            Defaults to 'x'.

    Returns:
        The ttk.Frame widget that was created.
    """
    frame = ttk.Frame(window)
    frame.pack(padx=padx, pady=pady, fill=fill)
    return frame


def create_single_line_entry(
    frame: ttk.Frame,
    font: WidgetFont,
    name: str,
    width: int = 28,
    side: str = RIGHT,
    padx: int = 5,
    pady: int = 3,
) -> ttk.Entry:
    """
    Create a single-line entry widget and add it to a frame.

    Args:
        frame (ttk.Frame):
            The ttk.Frame to which the entry should be added.
        font (WidgetFont): The font for the label.
        name (str): The name to use for the entry.
        width (int, optional): The width of the entry in characters.
            Defaults to 28.
        side (str, optional): The side of the frame on which to place
            the entry. Defaults to RIGHT.
        padx (int, optional): The horizontal padding for the date entry.
            Defaults to 5.
        pady (int, optional): The vertical padding for the date entry.
            Defaults to 3.

    Returns:
        The ttk.Entry widget that was created.
    """
    entry = ttk.Entry(frame, width=width, name=name)
    entry.pack(side=side, padx=padx, pady=pady)
    entry.config(font=font)
    return entry


def create_multi_line_entry(
    frame: ttk.Frame,
    font: tuple,
    name: str,
    height: int = 2,
    width: int = 28,
    side: str = RIGHT,
    padx: int = 5,
    pady: int = 3,
) -> ttk.Text:
    """
    Create a multi-line entry widget and add it to a frame.

    Args:
        frame (ttk.Frame):
            The ttk.Frame to which the entry should be added.
        font (WidgetFont): The font for the entry.
        name (str): The name to use for the entry.
        height (int, optional): The height of the entry in lines.
            Defaults to 2.
        width (int, optional): The width of the entry in characters.
            Defaults to 28.
        side (str, optional): The side of the frame on which to place
            the entry. Defaults to RIGHT.
        padx (int, optional): The horizontal padding for the entry.
            Defaults to 5.
        pady (int, optional): The vertical padding for the entry.
            Defaults to 3.

    Returns:
        The ttk.Text widget that was created.
    """
    entry = ttk.Text(frame, height=height, width=width, name=name)
    entry.pack(side=side, padx=padx, pady=pady)
    entry.config(font=font)
    return entry


def create_button(
    frame: ttk.Frame,
    text: str,
    command: callable,
    side: str = LEFT,
    height: int = 10,
    width: int = 5,
    padx: int = 5,
    pady: int = 5,
    font: tuple = ("Arial", 14),
) -> ttk.Button:
    """
    Create a button widget and add it to a frame.

    Args:
        frame (ttk.Frame):
            The ttk.Frame to which the button should be added.
        text (str): The text to be displayed on the button.
        command (callable): The function to be called when the button is
            clicked.
        side (str, optional): The side of the frame on which to place
            the button. Defaults to LEFT.
        height (int, optional): The height of the button in pixels.
            Defaults to 10.
        width (int, optional): The width of the button in pixels.
            Defaults to 5.
        padx (int, optional): The horizontal padding for the button.
            Defaults to 5.
        pady (int, optional): The vertical padding for the button.
            Defaults to 5.
        font (WidgetFont, optional): The font for the button.
            Defaults to ("Arial", 14).

    Returns:
        The ttk.Button widget that was created.
    """
    font_style = ttk.Style()
    font_style.configure("Bold.TButton", font=font)

    button = ttk.Button(
        frame,
        text=text,
        command=command,
        style="Bold.TButton",
    )
    button.pack(padx=padx, pady=pady, side=side, ipady=height, ipadx=width)
    return button


def create_date_entries(app: ttk.Window, date_labels: dict) -> dict:
    """
    Create date entries and add them to a frame in the app.

    Args:
        app (ttk.Window):
            The main application window.
        date_labels (dict):
            A dictionary with keys as the label for the date entries,
            and values as the name to use for the entries

    Returns:
        A dictionary with the created ttk.Entry widgets, where keys are
        the names of the entries, and values are the ttk.Entry widgets
        themselves.
    """
    user_input_objects = {}
    for label, name in date_labels.items():
        frame = create_frame(app)
        user_input_objects[name] = create_date_entry(
            frame=frame, label_text=label, name=name
        )
    return user_input_objects


def create_single_line_entries(
    app: ttk.Window,
    single_line_labels: dict,
) -> dict:
    """
    Create single-line entries and add them to a frame in the app.

    Args:
        app (ttk.Window):
            The main application window.
        single_line_labels (dict):
            A dictionary with keys as the label for the single-line
            entries, and values as the name to use for the entries.

    Returns:
        A dictionary with the created ttk.Entry widgets, where keys are
        the names of the entries, and values are the ttk.Entry widgets
        themselves.
    """
    user_input_objects = {}
    for label, name in single_line_labels.items():
        frame = create_frame(app)
        user_input_objects[name] = create_label_entry(
            frame=frame, label_text=label, name=name
        )
    return user_input_objects


def create_multi_line_entries(
    app: ttk.Window,
    multi_line_labels: dict,
) -> dict:
    """
    Create multi-line entries and add them to a frame in the app.

    Args:
        app (Window):
            The main application window.
        multi_line_labels (dict):
            A dictionary with keys as the label for the multi-line
            entries, and values as the name to use for the entries.

    Returns:
        A dictionary with the created ttk.Text widgets, where keys are
        the names of the entries, and values are the ttk.Text widgets
        themselves.
    """
    user_input_objects = {}
    for label, name in multi_line_labels.items():
        frame = create_frame(app)
        user_input_objects[name] = create_label_entry(
            frame=frame, label_text=label, name=name, multi_line=True
        )
    return user_input_objects


def create_buttons(app: ttk.Window, buttons: dict) -> None:
    """
    Create buttons and add them to a frame in the app.

    Args:
        app (ttk.Window):
            The main application window.
        buttons (dict):
            A dictionary with keys as the label for the buttons, and
            values as the functions to be called when the buttons are clicked.

    Returns:
        None.
    """

    frame = create_frame(app)
    for button_label, button_function in buttons.items():
        create_button(frame=frame, text=button_label, command=button_function)
