#!/usr/bin/python3
"""adds all arguments to a Python list, and then saves them to a file"""

import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argsTokenized = []
if os.path.exists("add_item.json"):
    argsTokenized = load_from_json_file("add_item.json")
save_to_json_file(argsTokenized + sys.argv[1:], "add_item.json")
