import random

class ChordNode:
    def __init__(self, node_id, m, nodes):
        self.id = node_id
        self.m = m
        self.nodes = sorted(nodes)
        self.finger_table = []

    def find_successor(self, key):
        for node in self.nodes:
            if node >= key:
                return node
        return self.nodes[0]

    def build_finger_table(self):
        self.finger_table = []
        for i in range(self.m):
            start = (self.id + 2**i) % (2**self.m)
            successor = self.find_successor(start)
            self.finger_table.append((start, successor))

    def closest_preceding_node(self, key):
        for start, node in reversed(self.finger_table):
            if self.id < node < key:
                return node
        return self.id


def chord_lookup(start_node, key, node_objects):
    path = [start_node]
    current = start_node

    while True:
        node = node_objects[current]
        successor = node.find_successor(key)

        if current == successor:
            break

        next_node = node.closest_preceding_node(key)

        if next_node == current:
            next_node = successor

        path.append(next_node)
        current = next_node

        if current == successor:
            path.append(successor)
            break

    return path