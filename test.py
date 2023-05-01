class Node:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Node({self.value})"

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.source}, {self.destination}, {self.weight})"

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        if not self.has_node(node):
            self.nodes.append(node)

    def has_node(self, node):
        for n in self.nodes:
            if n.value == node.value:
                return True
        return False

    def add_edge(self, edge):
        if self.has_node(edge.source) and self.has_node(edge.destination):
            self.edges.append(edge)
        else:
            print("Source and/or destination node not found in graph.")

    def get_nodes(self):
        for node in self.nodes:
            print(node.value)
        return self.nodes

    def get_edges(self):
        for edge in self.edges:
            print(edge.source.value, edge.destination.value, edge.weight)
        return self.edges

# # Create some nodes
# a = Node("A")
# b = Node("B")
# c = Node("C")
#
# # Create some edges
# e1 = Edge(a, b, 2)
# e2 = Edge(b, c, 3)
# e3 = Edge(c, a, 1)
#
# # Create a directed graph
# g = Graph()
#
# # Add the nodes and edges to the graph
# g.add_node(a)
# g.add_node(b)
# g.add_node(c)
# g.add_edge(e1)
# g.add_edge(e2)
# g.add_edge(e3)
#
# # Try to add a node that already exists in the graph
# g.add_node(Node("B"))  # This should not add a duplicate node
#
# # Try to add an edge with a node that is not in the graph
# d = Node("D")
# e4 = Edge(b, d, 2)
# g.add_edge(e4)  # This should raise a ValueError
# print(g.get_nodes())
# print(g.get_edges())
