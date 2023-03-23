import datetime
from helpers.job_number_storage import JobNumbers


def generate_new_fn(self):
    """Generates a new, unassigned file number"""

    highest_existing_fn = max(file_numbers)
    last_four_digits = str(int(highest_existing_fn[4:8]) + 1)
    if len(last_four_digits) < 4:
        last_four_digits = "0" + last_four_digits
    new_fn = first_four + last_four_digits


class JobNumberGenerator:
    def __init__(self, job_number_storage: JobNumbers):
        self.job_number_storage = job_number_storage
        self.existing_job_numbers = self.job_number_storage.get_job_numbers()

    @property
    def job_number_prefix(self, num_previous_months: int = 0) -> str:
        now = datetime.datetime.now()
        year = now.year % 100
        month = now.month

        if num_previous_months > 0 and month > 1:
            month = f"{int(month)-num_previous_months}"

        job_number_prefix = f"{year}{month}"
        return job_number_prefix

    @property
    def job_number_suffix(self):
        job_number_prefix = self.job_number_prefix

    @property
    def unused_job_number(self):
        while True:
            job_numbers = [
                number
                for number in existing_job_numbers
                if number.startswith(self.job_number_prefix())
            ]
            if len(job_numbers) == 0:
                num_previous_months += 1
            else:
                break

        return int(max(job_numbers)) + 1


print(JobNumberGenerator().unused_job_number)
