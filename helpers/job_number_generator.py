"""This module contains the JobNumberGenerator class, which is used to
generate new job numbers."""

import datetime
from .job_number_storage import JobNumbers


class JobNumberGenerator:
    """This class is used to generate new job numbers."""

    def __init__(self, job_storage: JobNumbers):
        self.job_storage = job_storage
        self.now = datetime.datetime.now()
        self.year = self.now.year % 100
        self.month = self.now.month

    def get_job_number_prefix(self, num_previous_months: int = 0) -> str:
        """Returns the prefix for a job number based on the current year
        and month."""
        month = self.month
        if num_previous_months > 0 and month > 1:
            month -= num_previous_months
            if month < 1:
                month += 12

        job_number_prefix = f"{self.year:02d}{month:02d}"
        return job_number_prefix

    @property
    def unused_job_number(self) -> str:
        """Returns the next unused job number based on the current year
        and month."""
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
