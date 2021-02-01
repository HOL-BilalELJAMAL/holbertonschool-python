#!/usr/bin/python3
"""
    100-singly_linked_list.py
    Module that defines a linked list
    Include 2 classes called Node and SinglyLinkedList
"""


class Node:
    """
    Represents a class called Node with:
        private instance attribute called data
        private instance attribute called next_node
    """

    def __init__(self, data, next_node=None):
        """Initialization of the private instance attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter property to get the data of the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node
        Args:
            value (int): New data of the Square
        Note:
            If data is not an integer, a TypeError exception is raised
            Otherwise, Successful Set
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter property to get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node
        Args:
            value (Node): Next node of the Square
        Note:
            If next_node is not a Node, a TypeError exception is raised
            Otherwise, Successful Set
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a class called SinglyLinkedList with:
        private instance attribute called head
    """

    def __init__(self):
        """Initialization of the private instance attribute"""
        self.__head = None

    def sorted_insert(self, value):
        """Function that insert a node based on its sorted value"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        curr = self.__head
        while value >= curr.data:
            prev = curr
            if curr.next_node:
                curr = curr.next_node
            else:
                curr.next_node = new_node
                return
        prev.next_node = new_node
        new_node.next_node = curr

    def __str__(self):
        """Function that define the format of the node representation"""
        string = ""
        curr = self.__head
        while curr:
            string += str(curr.data) + "\n"
            curr = curr.next_node
        return string[:-1]
