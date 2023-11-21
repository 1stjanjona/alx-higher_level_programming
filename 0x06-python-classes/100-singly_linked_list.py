#!/usr/bin/python3
"""Class Node that defines a node of a singly linked list."""


class Node:
    """Define a node of singly linked list."""

    def __init__(self, data, next_node=None):
        """Init a node.

        Args:
            data: data of node should be int.
            next_node: next node of the node.
        """
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        """Set the node data."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """set next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Define SinglyLinkedList."""

    def __init__(self):
        """init SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """insert new Node.

        Args:
            value (Node): inserted new node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Printable singly linked list."""
        list_numbers = []
        tmp = self.__head
        while tmp is not None:
            list_numbers.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(list_numbers))
