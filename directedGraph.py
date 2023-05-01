from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.incoming_arcs = []
        self.outgoing_arcs = []

    def add_outgoing_arc(self, arc):
        self.outgoing_arcs.append(arc)

    def add_incoming_arc(self, arc):
        # print(f"Node {self.value} with incoming arc added: {arc}")
        self.incoming_arcs.append(arc)

    def __repr__(self):
        return f"Node({self.value})"

    def get_outgoing_arcs(self):
        return self.outgoing_arcs

    def get_incoming_arcs(self):
        return self.incoming_arcs


class Arc:
    def __init__(self, start_node, end_node, weight=1):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
        start_node = start_node
        end_node = end_node

    def __repr__(self):
        return f"Arc({self.start_node.value}, {self.end_node.value}, {self.weight})"


class DirectedGraph:
    def __init__(self):
        self.nodes = []
        self.arcs = []

    def add_node(self, node):
        if self.node_exists(node) is not None:
            return
        self.nodes.append(node)

    def add_arc(self, arc):
        start_node = self.node_exists(arc.start_node)
        end_node = self.node_exists(arc.end_node)
        if start_node is not None and end_node is not None:
            start_node.add_outgoing_arc(arc)
            end_node.add_incoming_arc(arc)
            self.arcs.append(arc)

    def bfs(self, value):
        queue = deque()
        visited = set()
        for node in self.nodes:
            if node.value == value:
                return node
            queue.append(node)
            visited.add(node)
        while queue:
            curr_node = queue.popleft()
            for arc in curr_node.outgoing_arcs:
                dest_node = arc.end_node
                if dest_node not in visited:
                    if dest_node.value == value:
                        return dest_node
                    queue.append(dest_node)
                    visited.add(dest_node)
        return None

    def node_exists(self, node):
        # for n in self.nodes:
        #     if n.value == node.value:
        #         return n
        # return None
        return self.bfs(node.value)

    def __repr__(self):
        return f"DirectedGraph(nodes={self.nodes}, arcs={self.arcs})"

    def get_nodes(self):
        for node in self.nodes:
            print(f"Node {node.value} with outgoing arcs: {node.get_outgoing_arcs()}")
            print(f"Node {node.value} with incoming arcs: {node.get_incoming_arcs()}")


def test_run():
    # Create some nodes and arcs
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    arc1 = Arc(a, b)
    arc2 = Arc(a, c)
    arc3 = Arc(b, d)
    arc4 = Arc(c, d)
    arc5 = Arc(d, e)
    arc6 = Arc(c, f)

    # Create a graph and add the nodes and arcs to it
    graph = DirectedGraph()
    graph.add_node(a)
    graph.add_node(b)
    graph.add_node(c)
    graph.add_node(d)
    graph.add_node(e)
    graph.add_node(f)
    graph.add_arc(arc1)
    graph.add_arc(arc2)
    graph.add_arc(arc3)
    graph.add_arc(arc4)
    graph.add_arc(arc5)
    graph.add_arc(arc6)

    # graph.add_node(Node("B"))  # This should not add a duplicate node
    # Print the graph
    print(graph)
    print(graph.get_nodes())


if __name__ == '__main__':
    test_run()
