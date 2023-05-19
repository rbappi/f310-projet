class DirectedGraph:
    def __init__(self):
        self._nodes = {}
        self._arcs = {}

    def add_node(self, node):
        if self.node_exists(node) is False:
            self._nodes[node.get_value()] = node
            return

    def add_arc(self, arc):
        start_node_exists = self.node_exists(arc.start_node)
        end_node_exists = self.node_exists(arc.end_node)
        if start_node_exists is True and end_node_exists is True:
            self._nodes[arc.start_node.get_value()].add_outgoing_arc(arc)
            self._nodes[arc.end_node.get_value()].add_incoming_arc(arc)
            self._arcs[arc.get_id()] = arc

    def node_exists(self, node):
        return node.get_value() in self._nodes

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

    def get_arc_from_id(self, id):
        return self._arcs[id]

    def update_arc_flow(self, id, flow):
        self._arcs[id].set_flow(flow)

    def update_arc_capacity(self, id, capacity):
        self._arcs[id].set_cost(capacity)

    def arc_exists(self, arc_id):
        return arc_id in self._arcs
