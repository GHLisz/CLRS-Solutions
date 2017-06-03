import random
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil


def list_search(L, k):
    x = L.nil.next
    L.nil.key = k
    while x.key != k:
        x = x.next
    if x == L.nil:
        return None
    return x
