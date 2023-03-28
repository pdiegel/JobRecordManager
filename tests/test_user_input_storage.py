import unittest
from unittest.mock import MagicMock, patch
from functools import partial
import ttkbootstrap as ttk
from helpers import user_input_storage, job_number_storage
from helpers import job_number_generator, database_connector


class TestUserInputStorage(unittest.TestCase):
    def setUp(self):
        self.user_input_storage = user_input_storage.UserInputStorage()

    def test_init(self):
        self.assertEqual(self.user_input_storage.input_objects, {})

    def test_add_inputs(self):
        input_objects = {
            "job_date": MagicMock(spec=ttk.DateEntry),
            "fieldwork_date": MagicMock(spec=ttk.DateEntry),
            "job_number": MagicMock(spec=ttk.Entry),
            "parcel_id": MagicMock(spec=ttk.Entry),
            "entry_by": MagicMock(spec=ttk.Entry),
            "requested_services": MagicMock(spec=ttk.Text),
            "contact_info": MagicMock(spec=ttk.Text),
            "additional_info": MagicMock(spec=ttk.Text),
        }
        self.user_input_storage.add_inputs(input_objects)
        self.assertEqual(self.user_input_storage.input_objects, input_objects)

    def test_clear(self):
        input_objects = {
            "job_date": MagicMock(spec=ttk.DateEntry),
            "fieldwork_date": MagicMock(spec=ttk.DateEntry),
            "job_number": MagicMock(spec=ttk.Entry),
            "parcel_id": MagicMock(spec=ttk.Entry),
            "entry_by": MagicMock(spec=ttk.Entry),
            "requested_services": MagicMock(spec=ttk.Text),
            "contact_info": MagicMock(spec=ttk.Text),
            "additional_info": MagicMock(spec=ttk.Text),
        }
        self.user_input_storage.add_inputs(input_objects)
        self.user_input_storage.clear()
        self.assertEqual(self.user_input_storage.input_objects, {})

    def test_inputs(self):
        job_date = MagicMock(spec=ttk.DateEntry)
        fieldwork_date = MagicMock(spec=ttk.DateEntry)
        job_number = MagicMock(spec=ttk.Entry)
        parcel_id = MagicMock(spec=ttk.Entry)
        entry_by = MagicMock(spec=ttk.Entry)
        requested_services = MagicMock(spec=ttk.Text)
        contact_info = MagicMock(spec=ttk.Text)
        additional_info = MagicMock(spec=ttk.Text)

        job_date.entry.get.return_value = "2023-03-27"
        fieldwork_date.entry.get.return_value = "2023-03-26"
        job_number.get.return_value = "1234"
        parcel_id.get.return_value = "5678"
        entry_by.get.return_value = "John Doe"
        requested_services.get.return_value = "Service request\n"
        contact_info.get.return_value = "Contact info\n"
        additional_info.get.return_value = "Additional info\n"

        input_objects = {
            "job_date": job_date,
            "fieldwork_date": fieldwork_date,
            "job_number": job_number,
            "parcel_id": parcel_id,
            "entry_by": entry_by,
            "requested_services": requested_services,
            "contact_info": contact_info,
            "additional_info": additional_info,
        }
        self.user_input_storage.add_inputs(input_objects)

        expected = {
            "job_date": "2023-03-27",
            "fieldwork_date": "2023-03-26",
            "job_number": "1234",
            "parcel_id": "5678",
            "entry_by": "John Doe",
            "requested_services": "Service request",
            "contact_info": "Contact info",
            "additional_info": "Additional info",
        }
        self.assertEqual(self.user_input_storage.inputs, expected)


if __name__ == "__main__":
    unittest.main()
