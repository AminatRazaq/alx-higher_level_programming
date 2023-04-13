#!/usr/bin/python3

"""Defines a JSON string to Object funtion"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) reps. by a JSON string"""
    return json.loads(my_str)
