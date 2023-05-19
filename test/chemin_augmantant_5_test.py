import os
import sys

sys.path.append(os.path.abspath(os.path.join('..', 'src')))

from arc import Arc
from chemin_augmentant_processor import CheminAugmentant, DirectedGraph, ProblemInfo
from chemin_augmentant import main as chemin_augmentant_main
from node import Node


def six_tester():
    # file = FileReader("../instances/inst-1000-0.3.txt")
    # graph = file.get_graph()
    # problemInfo = file.get_problem_info()
    chemin_augmentant_main("../instances/inst-1000-0.3.txt")


def five_tester():
    graph = DirectedGraph()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    arc1 = Arc(node1, node2, 15, 10)
    arc2 = Arc(node1, node3, 15, 10)
    arc3 = Arc(node2, node4, 15, 10)
    arc4 = Arc(node3, node4, 10, 10)
    arc5 = Arc(node3, node5, 10, 0)
    arc6 = Arc(node4, node5, 20, 20)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_node(node5)
    graph.add_arc(arc1)
    graph.add_arc(arc2)
    graph.add_arc(arc3)
    graph.add_arc(arc4)
    graph.add_arc(arc5)
    graph.add_arc(arc6)
    problemInfo = ProblemInfo()
    problemInfo.source = 1
    problemInfo.sink = 5
    chemin_augmentant = CheminAugmentant(graph, problemInfo)
    chemin_augmentant.chemin_augmentant(graph, problemInfo)
    l = chemin_augmentant.get_L()
    for node in l:
        print(f"{node}: {l[node]}")
    # print(chemin_augmentant.get_graph().print_nodes())
    # print(chemin_augmentant.get_graph())
    # print(f"Arcs after augmeting path: {chemin_augmentant.get_arcs()}")
    arcs = chemin_augmentant.get_arcs()
    for arc in arcs:
        print(f"{arcs[arc]}")


def main_tester():
    # timer = Timer()
    file_timer = open("../results/python/timer.txt", "w")
    for filename in os.listdir("../instances"):
        if filename.endswith("0.3.txt"):
            print(f"----------->Creating model for {filename}")
            # timer.start()
            time = chemin_augmentant_main(f"../instances/{filename}", "../results/python")
            # timer.stop()
            file_timer.write("-------------------------------------\n")
            file_timer.write(f"{filename}: {time}\n")
            file_timer.write("-------------------------------------\n")
            print(f"----------->Done with {filename}")
    file_timer.close()


if __name__ == "__main__":
    six_tester()
    # five_tester()
    # main_tester()
