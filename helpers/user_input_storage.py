from typing import List, Union
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class UserInputStorage:
    def __init__(
        self,
        input_objects: List[Union[ttk.DateEntry, ttk.Entry, ttk.Text]] = None,
    ):
        self.input_objects = input_objects or []

    def add_inputs(
        self, input_objects: List[Union[ttk.DateEntry, ttk.Entry, ttk.Text]]
    ):
        self.input_objects.extend(input_objects)

    def clear(self):
        self.input_objects.clear()

    @property
    def inputs(self) -> List[str]:
        user_inputs = {}
        for input_object in self.input_objects:
            object_name = input_object._name
            if isinstance(input_object, ttk.DateEntry):
                object_contents = input_object.entry.get()
            elif isinstance(input_object, ttk.Entry):
                object_contents = input_object.get()
            elif isinstance(input_object, ttk.Text):
                object_contents = input_object.get("1.0", "end-1c")
            user_inputs[object_name] = object_contents
        return user_inputs
