from chemin_augmentant import CheminAugmentant, DirectedGraph, ProblemInfo, Node
from arc import ArcWithFlow
from lp_handler import FileReader


def six_tester():
    file = FileReader("../instances/inst-100-0.3.txt")
    graph = file.get_graph()
    problemInfo = file.get_problem_info()
    chemin_augmentant = CheminAugmentant(graph, problemInfo)
    chemin_augmentant.chemin_augmentant(graph, problemInfo)
    print(chemin_augmentant.get_graph())
    print(chemin_augmentant.get_L())

def five_tester():
    graph = DirectedGraph()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    arc1 = ArcWithFlow(node1, node2, 15, 10)
    arc2 = ArcWithFlow(node1, node3, 15, 10)
    arc3 = ArcWithFlow(node2, node4, 15, 10)
    arc4 = ArcWithFlow(node3, node4, 10, 10)
    arc5 = ArcWithFlow(node3, node5, 10, 0)
    arc6 = ArcWithFlow(node4, node5, 20, 20)
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


if __name__ == "__main__":
    six_tester()
    # five_tester()