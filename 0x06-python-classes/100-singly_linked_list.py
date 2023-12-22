#!/usr/bin/python3
"defines a singly linked list"


class Node:
    "defines a Node in SinglyLinkedList"

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None:
            if type(value) is not Node:
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    "defines a SinglyLinkedList"

    def __init__(self):
        self.__head = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        current = self.__head
        if current is None:
            return ''
        r = ''
        while current.next_node:
            r += str(current.data) + '\n'
            current = current.next_node
        r += str(current.data)
        return r

    def sorted_insert(self, value):
        prev = None
        new = Node(data=value)
        current = self.__head
        # empty list
        if not current:
            self.__head = new
            return
        # one item
        if not current.next_node:
            if current.data < value:
                current.next_node = new
                return
            else:
                self.__head = new
                new.next_node = current
                return
        # two items or more
        while current.next_node:
            if current.data < value:
                prev = current
                current = current.next_node
                continue
            else:
                break
        if not prev:
            self.__head = new
            new.next_node = current
            return
        if current.data < value:
            new.next_node = current.next_node
            current.next_node = new
            return
        else:
            prev.next_node = new
            new.next_node = current
            return
