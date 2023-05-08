import sys
from directed_graph import DirectedGraph
from arc import Arc
from lp_handler import FileReader
from node import Node
from problem_info import ProblemInfo


class CheminAugmentant:

    def __init__(self, graph: DirectedGraph, prob_info: ProblemInfo):
        self._graph = graph
        self._prob_info = prob_info
        self._L = {}
        self._L_values = {}
        self._visited = {}
        self._start_node = self._graph.get_node_from_value(self._prob_info.source)
        self.initialize()

    def initialize(self):
        self._L_values = {self._start_node.get_value(): [None, None, float("inf")]}  # [parent, arc, alpha]
        self._L = {self._start_node: [None, None, float("inf")]}
        self._visited = {self._start_node: True}

    def mark_node(self, node):
        if self._prob_info.sink == node.get_value():
            return self._L_values
        else:
            for outgoing_arc in node.get_outgoing_arcs():
                if outgoing_arc.get_end_node().get_value() not in self._L_values and outgoing_arc.get_flow() < outgoing_arc.get_capacity():
                    alpha_i = min(self._L[node][2], outgoing_arc.get_capacity() - outgoing_arc.get_flow())
                    self._L[outgoing_arc.get_end_node()] = [node, outgoing_arc, alpha_i]
                    self._L_values[outgoing_arc.get_end_node().get_value()] = [node, outgoing_arc, alpha_i]

            for incoming_arc in node.get_incoming_arcs():
                if incoming_arc.get_start_node().get_value() not in self._L_values and incoming_arc.get_flow() > 0:
                    alpha_i = min(self._L[node][2], incoming_arc.get_flow())
                    self._L[incoming_arc.get_start_node()] = [node, incoming_arc, alpha_i]
                    self._L_values[incoming_arc.get_start_node().get_value()] = [node, incoming_arc, alpha_i]

            self._visited[node] = True
            self._L.pop(node)
            for node in self._L:
                if node not in self._visited:
                    return self.mark_node(node)
                    # if ret is True:
                    #     return True
            # return self._L_values

    def get_direction(self, arc, father):
        if arc.get_start_node() == father:
            return True
        else:
            return False

    def augmented_path(self):
        actual_value = self._prob_info.sink
        while actual_value != self._prob_info.source:
            father = self._L_values[actual_value][0]
            arc_from_l = self._L_values[actual_value][1]
            arc_id = arc_from_l.get_id()
            forward = self.get_direction(arc_from_l, father)
            if forward is True:
                new_flow = arc_from_l.get_flow() + self._L_values[actual_value][2]
                self._graph.update_arc_flow(arc_id, new_flow)
            else:
                new_flow = arc_from_l.get_flow() - self._L_values[actual_value][2]
                self._graph.update_arc_flow(arc_id, new_flow)
            actual_value = father.get_value()

    def get_max_flow(self):
        max_flow = 0
        for arc in self._graph.get_node_from_value(self._prob_info.source).get_outgoing_arcs():
            max_flow += arc.get_flow()
        for arc in self._graph.get_node_from_value(self._prob_info.sink).get_incoming_arcs():
            max_flow -= arc.get_flow()
        return max_flow

    def get_graph(self):
        return self._graph.print_nodes()

    def chemin_augmentant(self, graph: DirectedGraph, prob_info: ProblemInfo):
        """
        Returns a list of arcs that form a path from source to sink, if such a path exists.
        """
        L_copy = {self._prob_info.sink: True}
        iteration = 0
        while self._prob_info.sink in L_copy:
            L_copy = self.mark_node(self._start_node)
            self.augmented_path()
            self.initialize()
            iteration += 1
            print(f"Iteration {iteration}")


    def get_L(self):
        return self._L

    def get_graph(self):
        return self._graph


def read_file(file, dest="./"):
    fl = FileReader(file)
    graph = fl.get_graph()
    problemInfo = fl.get_problem_info()
    chemin_augmentant = CheminAugmentant(graph, problemInfo)
    chemin_augmentant.chemin_augmentant(graph, problemInfo)
    print(chemin_augmentant.get_L())
    print(chemin_augmentant.get_graph().print_nodes())
    print(chemin_augmentant.get_graph())


if __name__ == "__main__":
    length = len(sys.argv)
    if length < 2:
        print("Usage: python3 generate_model.py <filename> [<destination>]")
        exit(1)
    filename = sys.argv[1]
    if length == 3:
        destination = sys.argv[2]
        read_file(filename, destination)
    else:
        read_file(filename)
