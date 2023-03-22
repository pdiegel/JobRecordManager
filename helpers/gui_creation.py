import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def create_label_entry(
    frame: ttk.Frame,
    label_text: str,
    name: str,
    label_font: tuple = ("Arial", 14),
    entry_font: tuple = ("Arial", 12),
    multi_line: bool = False,
) -> None:
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
    label_font: tuple = ("Arial", 14),
    bootstyle: str = "primary",
    padx: int = 5,
    pady: int = 3,
    fill: str = X,
) -> None:
    create_label(frame, label_text, label_font)

    date_entry = ttk.DateEntry(frame, bootstyle=bootstyle, name=name)
    date_entry.pack(pady=pady, padx=padx, fill=fill)
    return date_entry


def create_label(
    frame: ttk.Frame,
    text: str,
    font: tuple,
    side: str = LEFT,
    padx: int = 5,
    pady: int = 3,
) -> ttk.Label:
    label = ttk.Label(frame, text=text)
    label.pack(side=side, padx=padx, pady=pady)
    label.config(font=font)
    return label


def create_frame(
    window: ttk.Window, padx: int = 10, pady: int = 5, fill: str = X
) -> ttk.Frame:
    frame = ttk.Frame(window)
    frame.pack(padx=padx, pady=pady, fill=fill)
    return frame


def create_single_line_entry(
    frame: ttk.Frame,
    font: tuple,
    name: str,
    width: int = 28,
    side: str = RIGHT,
    padx: int = 5,
    pady: int = 3,
) -> ttk.Entry:
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
    font_style = ttk.Style()
    font_style.configure("Bold.TButton", font=font)

    button = ttk.Button(
        frame, text=text, command=command, style="Bold.TButton"
    )
    button.pack(padx=padx, pady=pady, side=side, ipady=height, ipadx=width)
    return button
