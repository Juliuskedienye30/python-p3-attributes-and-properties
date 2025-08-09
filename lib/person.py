#!/usr/bin/env python3

# List of approved job titles
APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unknown"):
        """
        Initialize a new Person instance.
        Uses the property setters so that validation occurs automatically.
        """
        self.name = name  # Calls the name setter
        self.job = job    # Calls the job setter

    # -----------------
    # name property
    # -----------------
    def get_name(self):
        """Return the person's name."""
        return self._name

    def set_name(self, value):
        """
        Set the person's name.
        - Must be a string.
        - Must be between 1 and 25 characters.
        - Will be converted to title case before storing.
        If invalid, print an error message.
        """
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # -----------------
    # job property
    # -----------------
    def get_job(self):
        """Return the person's job title."""
        return self._job

    def set_job(self, value):
        """
        Set the person's job title.
        - Must be in the APPROVED_JOBS list.
        If invalid, print an error message.
        """
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
