#!/usr/bin/python3
"""
    0-lockboxes.py
    Module that defines a function called canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Function that checks if all boxes can be unlocked

    Args:
        boxes (list): list of boxes list

    Note:
        All keys will be positive integers
        A key with the same number as a box opens that box
        Return True if all boxes can be opened, else return False
    """
    boxes_keys = [0]
    for box_key in boxes_keys:
        for key in boxes[box_key]:
            if key < len(boxes) and key not in boxes_keys:
                boxes_keys.append(key)
    return len(boxes_keys) == len(boxes)
