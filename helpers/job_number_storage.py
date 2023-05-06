"""This module contains the JobNumbers class, which is used to store job
numbers."""


class JobNumbers:
    """This class is used to store job numbers."""

    def __init__(self):
        self.current_year_job_numbers = set()
        self.existing_job_numbers = set()
        self.active_job_numbers = set()
        self.unused_job_number = ""

    def add_job_number(self, job_number: str) -> None:
        """Adds a job number to the set of existing job numbers and the
        set of active job numbers."""
        self.existing_job_numbers.add(job_number)
        self.active_job_numbers.add(job_number)

    def remove_job_number(self, job_number: str) -> None:
        """Removes a job number from the set of active job numbers."""
        self.existing_job_numbers.remove(job_number)

    def add_existing_job_numbers(self, job_numbers: tuple) -> None:
        """Adds existing job numbers to the set of existing job numbers."""
        # Pulling from access database as a tuple, with job number being
        # the first element.
        job_numbers = [job_number[0] for job_number in job_numbers]
        self.existing_job_numbers.update(job_numbers)

    def add_active_job_numbers(self, job_numbers: tuple) -> None:
        """Adds active job numbers to the set of active job numbers."""
        # Pulling from access database as a tuple, with job number being
        # the first element.
        job_numbers = [job_number[0] for job_number in job_numbers]
        self.active_job_numbers.update(job_numbers)

    def add_current_year_job_numbers(self, job_numbers: tuple) -> None:
        """Adds current year job numbers to the set of current year job
        numbers."""
        # Pulling from access database as a tuple, with job number being
        # the first element.
        job_numbers = [job_number[0] for job_number in job_numbers]
        self.current_year_job_numbers.update(job_numbers)

    def clear_job_numbers(self) -> None:
        """Clears all existing and active job numbers."""
        self.existing_job_numbers.clear()
        self.active_job_numbers.clear()

    def get_existing_job_numbers(self) -> list[str]:
        """Returns a list of existing job numbers."""
        return self.existing_job_numbers

    def get_active_job_numbers(self) -> list[str]:
        """Returns a list of active job numbers."""
        return self.active_job_numbers

    def get_current_year_job_numbers(self) -> list[str]:
        """Returns a list of current year job numbers."""
        return self.current_year_job_numbers

    def add_unused_job_number(self, job_number: str) -> None:
        """Sets the unused job number."""
        self.unused_job_number = job_number
