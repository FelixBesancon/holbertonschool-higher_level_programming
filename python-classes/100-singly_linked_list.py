#!/usr/bin/python3
"""
This module defines:
    The class Node with:
        Private instance attributes:
            data.
            next_node.
        Private instance property and setters:
            data.
            next_node.
    The class SinglyLinkedList with:
        Private instance attribute:
            head.
        Public instance method:
            sorted_insert.
"""


class Node:
    """
    Represents a node of a singly linked list,
    with data and next_node.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance with :
            data.
            next_node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the current data of the current node.
        """
        return self.__data

    @property
    def next_node(self):
        """
        Retrieves the link to the next node of the current node.
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        Sets the data of the current node after validation.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node of the current node after validation.

        Raises:
            TypeError: If next_node is neither a Node or None.
        """
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list, with a head.
    """
    def __init__(self):
        """
        Initializes a singly linked list with:
            head.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of a singly linked list,
        with one node number by line.
        """
        sll_str = ""
        current = self.__head
        while current is not None:
            sll_str += str(current.data)
            if current.next_node is not None:
                sll_str += '\n'
            current = current.next_node
        return sll_str

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the singly linked list, in increasing order
        """
        current = self.__head
        previous = None
        while current is not None and value > current.data:
            previous = current
            current = current.next_node
        new_node = Node(value, current)
        if previous is None:
            self.__head = new_node
        else:
            previous.next_node = new_node
