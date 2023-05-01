# from nodes import Node
# from arcs import Arc


class Arc:

    def __init__(self, start, end, weight: int):
        self._start = start
        self._end = end
        self._weight = weight

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def weight(self):
        return self._weight

    @start.setter
    def start(self, start):
        self._start = start

    @end.setter
    def end(self, end):
        self._end = end

    @weight.setter
    def weight(self, weight):
        self._weight = weight


class Node:

    def __init__(self, id) -> None:
        self._id = id
        self._outgoingArcs = []
        self._incomingArcs = []

    @property
    def id(self):
        return self._id

    @property
    def outgoingArcs(self):
        return self._outgoingArcs

    @property
    def incomingArcs(self):
        return self._incomingArcs

    @outgoingArcs.setter
    def outgoingArcs(self, outgoingArcs):
        self._outgoingArcs = outgoingArcs

    @incomingArcs.setter
    def incomingArcs(self, incomingArcs):
        self._incomingArcs = incomingArcs

    def addOutgoingArc(self, arc: Arc):
        self._outgoingArcs.append(arc)

    def addIncomingArc(self, arc: Arc):
        self._incomingArcs.append(arc)



class Graph:

    def __init__(self) -> None:
        self._nodes = []
        self._arcs = []

    @property
    def nodes(self):
        return self._nodes

    @property
    def arcs(self):
        return self._arcs

    @nodes.setter
    def nodes(self, nodes):
        self._nodes = nodes

    @arcs.setter
    def arcs(self, arcs):
        self._arcs = arcs

    def addNode(self, node: Node):
        for n in self._nodes:
            if n.id == node.id:
                return
        self._nodes.append(node)

    def addArc(self, arc: Arc):
        self._arcs.append(arc)

    def getArc(self, start: Node, end: Node):
        for arc in self._arcs:
            if arc.start == start and arc.end == end:
                return arc
        return None

    def getArcs(self, start: Node, end: Node):
        arcs = []
        for arc in self._arcs:
            if arc.start == start and arc.end == end:
                arcs.append(arc)
        return arcs

    def getArcsFrom(self, start: Node):
        arcs = []
        for arc in self._arcs:
            if arc.start == start:
                arcs.append(arc)
        return arcs

    def getArcsTo(self, end: Node):
        arcs = []
        for arc in self._arcs:
            if arc.end == end:
                arcs.append(arc)
        return arcs

    def getGraph(self):

        for node in self._nodes:
            print(f"Nodes: {node.id}")
            print("outgoings: ")
            for arc in node.outgoingArcs:
                print(arc.end.id, end=" ")
            print("incomings: ", end=" ")
            for arc in node.incomingArcs:
                print(arc.start.id, end=" ")
        print("\n")
        for arc in self._arcs:
            print(arc.start.id, "->", arc.end.id, ": weight: ", arc.weight)


def runTest():
    graph = Graph()

    node1 = Node("A")
    graph.addNode(node1)  # add node1 to the graph

    node2 = Node("B")
    graph.addNode(node2)  # add node2 to the graph

    graph.addNode(node1)  # node1 already exists in the graph, so it won't be added again
    graph.getGraph()


if __name__ == "__main__":
    runTest()