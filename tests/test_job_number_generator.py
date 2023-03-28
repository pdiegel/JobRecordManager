import unittest
from datetime import datetime
from helpers.job_number_storage import JobNumbers
from helpers.job_number_generator import JobNumberGenerator


class MockJobNumberStorage(JobNumbers):
    def __init__(self, job_numbers=None):
        self.job_numbers = job_numbers or []

    def get_existing_job_numbers(self):
        return self.job_numbers

    def get_current_year_job_numbers(self):
        return self.job_numbers


class TestJobNumberGenerator(unittest.TestCase):
    def test_get_job_number_prefix(self):
        job_storage = MockJobNumberStorage()
        job_number_generator = JobNumberGenerator(job_storage)

        now = datetime.now()
        year = now.year % 100
        month = now.month
        expected_prefix = f"{year:02d}{month:02d}"

        self.assertEqual(
            job_number_generator.get_job_number_prefix(), expected_prefix
        )

    def test_unused_job_number(self):
        now = datetime.now()
        year = now.year % 100
        month = now.month
        existing_job_numbers = [
            "11110511",
            "23010105",
            "16030171",
            "23010111",
            "05120933",
            "22040237",
            "93121259",
            "22120530",
            "12050267",
        ]
        job_storage = MockJobNumberStorage(existing_job_numbers)
        job_number_generator = JobNumberGenerator(job_storage)

        expected_job_number = f"23030112"
        self.assertEqual(
            job_number_generator.unused_job_number, expected_job_number
        )

        expected_job_number = f"{year:02d}{month:02d}0101"


if __name__ == "__main__":
    unittest.main()
