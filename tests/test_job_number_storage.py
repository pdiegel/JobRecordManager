import unittest

from helpers.job_number_storage import JobNumbers

example_job_numbers = ["16030171", "23010111", "93121259"]


class TestJobNumbers(unittest.TestCase):
    def setUp(self):
        self.job_numbers = JobNumbers()

    def test_add_job_number(self):
        self.job_numbers.add_job_number(example_job_numbers[0])
        self.assertIn(
            example_job_numbers[0], self.job_numbers.existing_job_numbers
        )
        self.assertIn(
            example_job_numbers[0], self.job_numbers.active_job_numbers
        )

    def test_remove_job_number(self):
        self.job_numbers.add_job_number(example_job_numbers[0])
        self.job_numbers.remove_job_number(example_job_numbers[0])
        self.assertNotIn(
            example_job_numbers[0], self.job_numbers.existing_job_numbers
        )

    def test_add_existing_job_numbers(self):
        existing_job_numbers = [
            example_job_numbers[0],
            example_job_numbers[1],
            example_job_numbers[2],
        ]
        self.job_numbers.add_existing_job_numbers(existing_job_numbers)
        self.assertTrue(
            self.job_numbers.existing_job_numbers.issuperset(
                existing_job_numbers
            )
        )

    def test_add_active_job_numbers(self):
        active_job_numbers = [
            example_job_numbers[0],
            example_job_numbers[1],
            example_job_numbers[2],
        ]
        self.job_numbers.add_active_job_numbers(active_job_numbers)
        self.assertTrue(
            self.job_numbers.active_job_numbers.issuperset(active_job_numbers)
        )

    def test_clear_job_numbers(self):
        self.job_numbers.add_existing_job_numbers(
            [example_job_numbers[0], example_job_numbers[1]]
        )
        self.job_numbers.add_active_job_numbers([example_job_numbers[0]])
        self.job_numbers.clear_job_numbers()
        self.assertEqual(len(self.job_numbers.existing_job_numbers), 0)
        self.assertEqual(len(self.job_numbers.active_job_numbers), 0)


if __name__ == "__main__":
    unittest.main()
