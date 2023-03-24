class JobNumbers:
    def __init__(self):
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

    def clear_job_numbers(self):
        self.existing_job_numbers.clear()
        self.active_job_numbers.clear()

    def get_existing_job_numbers(self) -> list[str]:
        return self.existing_job_numbers

    def get_active_job_numbers(self) -> list[str]:
        return self.active_job_numbers

    def add_unused_job_number(self, job_number: str):
        self.unused_job_number = job_number
