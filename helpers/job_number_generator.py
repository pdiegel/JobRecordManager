import datetime
from .job_number_storage import JobNumbers


class JobNumberGenerator:
    def __init__(self, job_storage: JobNumbers):
        self.job_storage = job_storage
        self.now = datetime.datetime.now()
        self.year = self.now.year % 100
        self.month = self.now.month

    def get_job_number_prefix(self, num_previous_months: int = 0) -> str:
        month = self.month
        if num_previous_months > 0 and month > 1:
            month -= num_previous_months
            if month < 1:
                month += 12

        job_number_prefix = f"{self.year:02d}{month:02d}"
        return job_number_prefix

    @property
    def unused_job_number(self) -> str:
        num_previous_months = 0
        while num_previous_months < 12:
            prefix = self.get_job_number_prefix(num_previous_months)
            job_numbers = [
                number
                for number in self.job_storage.get_current_year_job_numbers()
                if number.startswith(prefix)
            ]
            if len(job_numbers) == 0:
                num_previous_months += 1
            else:
                highest_existing_fn = max(job_numbers)
                last_four_digits = str(
                    int(highest_existing_fn[4:8]) + 1
                ).zfill(4)
                new_fn = self.get_job_number_prefix() + last_four_digits
                break
        else:
            new_fn = self.get_job_number_prefix() + "0100"

        return new_fn


class JobNumbers:
    def __init__(self):
        self.current_year_job_numbers = set()
        self.existing_job_numbers = set()
        self.active_job_numbers = set()
        self.unused_job_number = ""

    def add_job_number(self, job_number: str):
        self.existing_job_numbers.add(job_number)
        self.active_job_numbers.add(job_number)

    def remove_job_number(self, job_number: str):
        self.existing_job_numbers.remove(job_number)

    def add_existing_job_numbers(self, job_numbers: tuple):
        # Pulling from access database as a tuple, with job number being
        # the first element.
        job_numbers = [job_number[0] for job_number in job_numbers]
        self.existing_job_numbers.update(job_numbers)

    def add_active_job_numbers(self, job_numbers: tuple):
        # Pulling from access database as a tuple, with job number being
        # the first element.
        job_numbers = [job_number[0] for job_number in job_numbers]
        self.active_job_numbers.update(job_numbers)

    def add_current_year_job_numbers(self, job_numbers: tuple):
        # Pulling from access database as a tuple, with job number being
        # the first element.
        job_numbers = [job_number[0] for job_number in job_numbers]
        self.current_year_job_numbers.update(job_numbers)

    def clear_job_numbers(self):
        self.existing_job_numbers.clear()
        self.active_job_numbers.clear()

    def get_existing_job_numbers(self) -> list[str]:
        return self.existing_job_numbers

    def get_active_job_numbers(self) -> list[str]:
        return self.active_job_numbers

    def get_current_year_job_numbers(self) -> list[str]:
        return self.current_year_job_numbers

    def add_unused_job_number(self, job_number: str):
        self.unused_job_number = job_number
