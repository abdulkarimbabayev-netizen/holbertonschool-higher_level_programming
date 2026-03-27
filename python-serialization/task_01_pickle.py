#!/usr/bin/python3
"""Module for pickling custom classes"""
import pickle


class CustomObject:
    """Custom class to serialize and deserialize"""

    def __init__(self, name, age, is_student):
        """Instantiation"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints object attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the object to a file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
