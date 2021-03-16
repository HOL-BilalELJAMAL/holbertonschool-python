#!/usr/bin/python3
"""
base.py
Module that defines a class called Base and returns a public instance attribute
called id
Including Method that converts list to JSON string
Including Method that writes a JSON string to a file
Including Method that converts JSON string to list
Including Method that returns a list of instances
Including Method that encodes list to CSV file
Including Method that decodes CSV file to list
"""

import json
import csv
import os.path


class Base:
    """
    Represents a class called Base with a public instance attribute
    called id
    """

    # A private class attribute, counting the number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the public instance attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function that return the JSON string representation of list

        Args:
            list_dictionaries (list): List of dictionaries

        Note:
            if list_dictionaries is None or empty, return empty list in string
            if list_dictionaries is not a list, a TypeError exception is raised
            if not all elements of list is not dictionary, a TypeError
            exception is raised
            Otherwise, Convert list_dictionaries to JSON string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(x) != dict for x in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that writes the JSON string representation of a list of
        objects to a file

        Args:
            list_objs (list): List of objects

        Note:
            if list_objs is not None or not a list, a TypeError exception is
            raised
            if list_objs is none or empty list, save empty list to file
            if not all elements of list are matching, a ValueError exception is
            raised
            Otherwise, writes JSON string representation of list to a file
        """
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            output = []
        else:
            first = type(list_objs[0])
            if any(type(x) != first for x in list_objs):
                raise ValueError("all elements of list_objs must match")
            output = [c.to_dictionary() for c in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
        """
        Function that returns the list of the JSON string representation

        Args:
            json_string (str): JSON string

        Note:
            if json_string is none or empty, return empty list
            if json_string is not a string, a TypeError exception is raised
            Otherwise, convert json_string to list

            If converted list elements are not dictionary, a ValueError
            exception is raised
            Otherwise, returns converted list
        """
        if json_string is None or json_string == "":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        loads = json.loads(json_string)
        for d in loads:
            if type(d) != dict:
                raise ValueError("json_string must contain dictionaries")
        return loads

    @classmethod
    def create(cls, **dictionary):
        """
        Function that returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            test = cls(1, 1)
        else:
            test = cls(1)
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances"""
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        res = []
        with open(filename, "r") as f:
            dicts = cls.from_json_string(f.readline())
        for d in dicts:
            res.append(cls.create(**d))
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that encodes a list to csv file"""
        if type(list_objs) != list and list_objs is not None \
                or not all(isinstance(x, cls) for x in list_objs):
            raise TypeError("list_objs must be a list")
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                rec_fields = ['id', 'width', 'height', 'x', 'y']
                squ_fields = ['id', 'size', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rec_fields)
                else:
                    writer = csv.DictWriter(f, fieldnames=squ_fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Function that decodes a csv file to a list"""
        filename = cls.__name__ + ".csv"
        rec_header = ["id", "width", "height", "x", "y"]
        squ_header = ["id", "size", "x", "y"]
        header = rec_header if cls.__name__ == "Rectangle" else squ_header
        res = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(new, header[j], int(e))
                        res.append(new)
        return res
