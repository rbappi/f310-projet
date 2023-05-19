from arc import Arc
from directed_graph import DirectedGraph
from node import Node


def main():
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
    graph.add_node(Node("B"))  # This should not add a duplicate node
    graph.add_arc(arc1)
    graph.add_arc(arc2)
    graph.add_arc(arc3)
    graph.add_arc(arc4)
    graph.add_arc(arc5)
    graph.add_arc(arc6)

    # graph.add_node(Node("B"))  # This should not add a duplicate node
    # Print the graph
    print(graph)
    print(graph.print_nodes())


if __name__ == '__main__':
    main()
