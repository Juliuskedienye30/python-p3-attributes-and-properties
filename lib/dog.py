#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Pug"):
        """
        Initialize a Dog instance.
        Default breed is 'Pug' so that when testing name errors,
        the breed validation does not also fail and print extra output.
        """
        self.name = name   # Calls name setter
        self.breed = breed # Calls breed setter

    # -----------------
    # name property
    # -----------------
    def get_name(self):
        """Return dog's name."""
        return self._name

    def set_name(self, value):
        """
        Validate and set dog's name.
        - Must be a string between 1 and 25 characters.
        If invalid, print only the name error message.
        """
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # -----------------
    # breed property
    # -----------------
    def get_breed(self):
        """Return dog's breed."""
        return self._breed

    def set_breed(self, value):
        """
        Validate and set dog's breed.
        - Must be in the APPROVED_BREEDS list.
        If invalid, print only the breed error message.
        """
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
