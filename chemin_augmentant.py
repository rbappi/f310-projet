import sys
from directed_graph import DirectedGraph
from arc import Arc
from lp_handler import FileReader
from node import Node
from problem_info import ProblemInfo


def chemin_augmentant(graph: DirectedGraph, prob_info: ProblemInfo):
    """
    Returns a list of arcs that form a path from source to sink, if such a path exists.
    """
    source = prob_info.source
    sink = prob_info.sink
    visited = set()
    queue = [source]
    parent = {source: None}
    while queue:
        node = queue.pop(0)
        if node == sink:
            break
        for arc in graph.get_node_from_value(node).get_outgoing_arcs():
            if arc.get_end_node() not in visited and arc.get_capacity() > 0:
                queue.append(arc.get_end_node())
                visited.add(arc.get_end_node())
                parent[arc.get_end_node()] = arc
    else:
        return None
    path = []
    current = sink
    while current != source:
        path.append(parent[current])
        current = parent[current].get_start_node()
    return path


def read_file(file, dest="./"):
    fl = FileReader(file)
    graph = fl.get_graph()
    problemInfo = fl.get_problem_info()
    print(chemin_augmentant(graph, problemInfo))


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
