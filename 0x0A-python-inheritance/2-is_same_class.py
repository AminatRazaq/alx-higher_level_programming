"""Defines function that returns True if the object or False"""


def is_same_class(obj, a_class):
    """Checks object is exactly an instance of the specified class

    Args:
        obj(any): the object checked
        a_class(any): The class to match the type of obj to

    Returns:
        True or False"""
    if type(obj) == a_class:
        return (True)
    return (False)
