from typing import Dict, TypeAlias, Union

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Define a type alias for the input objects
InputObject: TypeAlias = Union[ttk.DateEntry, ttk.Entry, ttk.Text]


class UserInputStorage:
    """
    A class for managing and storing user input objects and their
    values.
    """

    def __init__(self, input_objects: Dict[str, InputObject] = None) -> None:
        """
        Initializes the UserInputStorage object.

        Args:
            input_objects (Dict[str, InputObject], optional):
                A dictionary of input objects (widgets) indexed by their
                names. Defaults to an empty dictionary.
        """
        self.input_objects = input_objects or {}

    def add_inputs(self, input_objects: Dict[str, InputObject]) -> None:
        """
        Adds input objects (widgets) to the input_objects dictionary.

        Args:
            input_objects (Dict[str, InputObject]): A dictionary of
                input objects (widgets) indexed by their names.
        """
        self.input_objects.update(input_objects)

    def clear(self) -> None:
        """
        Clears the input_objects dictionary.
        """
        self.input_objects.clear()

    @property
    def inputs(self) -> Dict[str, str]:
        """
        Returns a dictionary containing the names and values of the
        input objects.

        Returns:
            Dict[str, str]:
                A dictionary of input object names and their values.
        """
        user_inputs = {}
        for object_name, input_object in self.input_objects.items():
            if isinstance(input_object, ttk.DateEntry):
                object_contents = input_object.entry.get()
            elif isinstance(input_object, ttk.Entry):
                object_contents = input_object.get()
            elif isinstance(input_object, ttk.Text):
                object_contents = input_object.get("1.0", "end-1c")
            user_inputs[object_name] = object_contents
        return user_inputs
