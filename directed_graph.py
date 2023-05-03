from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.incoming_arcs = []
        self.outgoing_arcs = []

    def add_outgoing_arc(self, arc):
        self.outgoing_arcs.append(arc)

    def add_incoming_arc(self, arc):
        self.incoming_arcs.append(arc)

    def __repr__(self):
        return f"Node({self.value})"

    def get_outgoing_arcs(self):
        return self.outgoing_arcs

    def get_incoming_arcs(self):
        return self.incoming_arcs


class Arc:
    def __init__(self, start_node, end_node, capacity=1):
        self._start_node = start_node
        self._end_node = end_node
        self._capacity = capacity
        self._id = f"x_{start_node.value}_{end_node.value}"

    def __repr__(self):
        return f"Arc(id: {self.id}, weight: {self._capacity})"

    def get_start_node(self):
        return self._start_node

    def get_end_node(self):
        return self._end_node

    def get_id(self):
        return self.id

    def get_capacity(self):
        return self._capacity

    @property
    def start_node(self):
        return self._start_node

    @property
    def end_node(self):
        return self._end_node

    @property
    def id(self):
        return self._id


class DirectedGraph:
    def __init__(self):
        self._nodes = {}
        self._arcs = []

    def add_node(self, node):
        if self.node_exists(node) is False:
            self._nodes[node.value] = node
            return

    def add_arc(self, arc):
        start_node_exists = self.node_exists(arc.start_node)
        end_node_exists = self.node_exists(arc.end_node)
        if start_node_exists is True and end_node_exists is True:
            self._nodes[arc.start_node.value].add_outgoing_arc(arc)
            self._nodes[arc.end_node.value].add_incoming_arc(arc)
            self._arcs.append(arc)

    def node_exists(self, node):
        return node.value in self._nodes

    def __repr__(self):
        return f"DirectedGraph(nodes={self._nodes}, arcs={self._arcs})"

    def print_nodes(self):
        for node in self._nodes:
            print(f"Node {node} with outgoing arcs: {self._nodes[node].get_outgoing_arcs()}")
            print(f"Node {node} with incoming arcs: {self._nodes[node].get_incoming_arcs()}")

    def get_nodes(self):
        return self._nodes

    def get_node_from_value(self, value):
        return self._nodes[value]

    def get_arcs(self):
        return self._arcs



