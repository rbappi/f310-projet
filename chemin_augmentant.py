import sys
from directed_graph import DirectedGraph
from file_handler import FileReader
from problem_info import ProblemInfo
from timer import Timer


class CheminAugmentant:

    def __init__(self, graph: DirectedGraph, prob_info: ProblemInfo):
        self._graph = graph
        self._prob_info = prob_info
        self._L = {}
        self._L_values = {}
        self._start_node = self._graph.get_node_from_value(self._prob_info.source)
        self._start_node_value = self._start_node.get_value()
        self.initialize()

    def initialize(self):
        self._L_values = {self._start_node_value: [None, None, float("inf")]}  # [parent (node), arc, alpha]
        self._L = {self._start_node: [None, None, float("inf")]} # [parent (value), arc, alpha]

    def marking_phase(self):
        actual_node = self._graph.get_node_from_value(self._start_node_value)
        if self._prob_info.sink == actual_node.get_value():
            return self._L_values

        while self._prob_info.sink not in self._L_values and len(self._L) != 0:

            for outgoing_arc in actual_node.get_outgoing_arcs():
                if outgoing_arc.get_end_node().get_value() not in self._L_values and outgoing_arc.get_flow() < outgoing_arc.get_capacity():
                    alpha_i = min(self._L_values[actual_node.get_value()][2],
                                  outgoing_arc.get_capacity() - outgoing_arc.get_flow())
                    end_node = self._graph.get_node_from_value(outgoing_arc.get_end_node().get_value())
                    self._L[end_node] = [actual_node, outgoing_arc, alpha_i]
                    self._L_values[outgoing_arc.get_end_node().get_value()] = [actual_node, outgoing_arc, alpha_i]

            for incoming_arc in actual_node.get_incoming_arcs():
                if incoming_arc.get_start_node().get_value() not in self._L_values and incoming_arc.get_flow() > 0:
                    alpha_i = min(self._L_values[actual_node.get_value()][2], incoming_arc.get_flow())
                    start_node = self._graph.get_node_from_value(incoming_arc.get_start_node().get_value())
                    self._L[start_node] = [actual_node, incoming_arc, alpha_i]
                    self._L_values[incoming_arc.get_start_node().get_value()] = [actual_node, incoming_arc, alpha_i]

            if self._prob_info.sink in self._L_values:
                return self._L_values

            self._L.pop(actual_node)
            if len(self._L) != 0:
                next_node = next(iter(self._L))
                actual_node = self._graph.get_node_from_value(next_node.get_value())

        return self._L_values

    def get_direction(self, arc, father):
        if arc.get_start_node().get_value() == father.get_value():
            return True
        else:
            return False

    def augmentation_phase(self):
        actual_value = self._prob_info.sink
        if actual_value not in self._L_values:
            return False
        actual_max_flow = self._L_values[actual_value][2]
        while actual_value != self._prob_info.source:
            father = self._L_values[actual_value][0]
            arc_from_l = self._L_values[actual_value][1]
            arc_id = arc_from_l.get_id()
            forward_from_father = self.get_direction(arc_from_l, father)
            if forward_from_father is True:
                new_flow = arc_from_l.get_flow() + actual_max_flow
                self._graph.update_arc_flow(arc_id, new_flow)
            else:
                new_flow = arc_from_l.get_flow() - actual_max_flow
                self._graph.update_arc_flow(arc_id, new_flow)
            actual_value = father.get_value()

    def get_max_flow(self):
        max_flow = 0
        for arc in self._graph.get_node_from_value(self._prob_info.source).get_outgoing_arcs():
            max_flow += arc.get_flow()
        return max_flow

    def get_graph(self):
        return self._graph.print_nodes()

    def chemin_augmentant(self, graph: DirectedGraph, prob_info: ProblemInfo):
        """
        Returns a list of arcs that form a path from source to sink, if such a path exists.
        """
        L_copy = {self._prob_info.sink: True}
        while self._prob_info.sink in L_copy:
            L_copy = self.marking_phase()
            self.augmentation_phase()
            self.initialize()

    def get_L(self):
        return self._L_values

    def get_graph(self):
        return self._graph

    def get_arcs(self):
        return self._graph.get_arcs()


def main(file, dest="./"):
    timer = Timer()
    fl = FileReader(file)
    graph = fl.get_graph()
    problem_info = fl.get_problem_info()
    chemin_augmentant = CheminAugmentant(graph, problem_info)
    print("---------------------------------")
    print("Running chemin augmentant...")
    timer.start()
    chemin_augmentant.chemin_augmentant(graph, problem_info)
    max_flow = chemin_augmentant.get_max_flow()
    timer.stop()
    print(f"Resolution complete in {timer.print_elapsed()}.")
    print(f"Max flow from source calculated: {max_flow}")
    arcs = chemin_augmentant.get_arcs()
    file_sol = f"model-{problem_info.nodes}-{problem_info.density}.path"
    file_to_write = open(file_sol, "w")
    print(f"Writing solution to '{file_sol}'...")
    file_to_write.write(f"Max flow from source calculated: {max_flow}\n")
    file_to_write.write(f"Resolution complete in {timer.print_elapsed()}.\n")
    for arc in arcs:
        # print(f"{arcs[arc]}")
        file_to_write.write(f"{arcs[arc]}\n")
    file_to_write.close()
    print("Done!")


if __name__ == "__main__":
    length = len(sys.argv)
    if length < 2 or length > 3:
        print("Usage: python3 generate_model.py <filename> [<destination>]")
        exit(1)
    filename = sys.argv[1]
    if length == 3:
        destination = sys.argv[2]
        main(filename, destination)
    else:
        main(filename)
