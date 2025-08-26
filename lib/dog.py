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

    # lib/dog.py

# lib/dog.py

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="", breed=""):
        self._name = None
        self._breed = None
        self.name = name
        # Only attempt to set breed if name is valid
        if self._name is not None:
            self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self._name = None
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
            self._breed = None
        else:
            self._breed = value

if __name__ == "__main__":
    dog1 = Dog("Buddy", "Beagle")
    print("Dog1:", dog1.name, dog1.breed)

    dog2 = Dog("", "Mastiff")
    print("Dog2:", dog2.name, dog2.breed)

    dog3 = Dog("Charlie", "AlienDog")
    print("Dog3:", dog3.name, dog3.breed)   

    dog4 = Dog("Luna", "Corgi")
    print("Dog 4:", dog4.name, dog4.breed)      

