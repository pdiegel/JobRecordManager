class JobNumbers:
    def __init__(self):
        self.existing_job_numbers = set()
        self.active_job_numbers = set()

    def add_job_number(self, job_number: str):
        self.existing_job_numbers.add(job_number)
        self.active_job_numbers.add(job_number)

    def remove_job_number(self, job_number: str):
        self.existing_job_numbers.remove(job_number)

    def add_existing_job_numbers(self, job_numbers: list[str]):
        self.existing_job_numbers.update(job_numbers)

    def add_active_job_numbers(self, job_numbers: list[str]):
        self.active_job_numbers.update(job_numbers)

    def clear_job_numbers(self):
        self.existing_job_numbers.clear()
        self.active_job_numbers.clear()

    def get_existing_job_numbers(self) -> list[str]:
        return list(self.existing_job_numbers).sort()

    def get_active_job_numbers(self) -> list[str]:
        return list(self.active_job_numbers).sort()
