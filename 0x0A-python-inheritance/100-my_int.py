#!/usr/bin/python3

"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts int operators == and !=."""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
