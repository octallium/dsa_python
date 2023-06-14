"""
Helper functions for checking equality between two objects.
"""


def isEqual(obj1: object, obj2: object) -> bool:
    """
    Compare two objects for equality.
    ---------------------------------

    Parameters:
    ----------
    obj1: object
          First object for comparison

    obj2: object
          Second object for comparison

    Returns:
    --------
    bool
        True if both the objects are equal
    """

    return True if obj1 is obj2 else obj1 == obj2


def checkAndDescribeEquality(obj1: object, obj2: object) -> None:
    """
    Compares and describes equality of two objects.
    -----------------------------------------------

    Parameters:
    ----------
    obj1: object
          First object for comparison

    obj2: object
          Second object for comparison

    Returns:
    --------
    None
    """

    if obj1 is obj2:
        print(f"{obj1} and {obj2} are the same object with id: {id(obj1)}")
    if obj1 == obj2:
        print(f"The values of {obj1} and {obj2} are the same.")
    if type(obj1) == type(obj2):
        print(f"{obj1} and {obj2} are of the same type: {type(obj1)}")
    else:
        print(f"{obj1} and {obj2} are NOT equal!")
