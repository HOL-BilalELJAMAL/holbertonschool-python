#!/usr/bin/python3
"""
    9-add_item.py
    Module that adds all arguments to a Python list, and then save
    them to a file
"""


import sys
import os.path

args = sys.argv[1:]

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

new_list = []

if os.path.exists("./add_item.json"):
    new_list = load_from_json_file("add_item.json")

save_to_json_file(new_list + args, "add_item.json")
