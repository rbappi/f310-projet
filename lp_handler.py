#!/usr/bin/python
from directed_graph import DirectedGraph, Node, Arc
from problem_info import ProblemInfo


class FileReader:
    def __init__(self, fileName) -> None:
        self._fileName = fileName
        self._problemInfo = ProblemInfo()
        self._graph = DirectedGraph()
        self._readFile()

    def _readFile(self):
        print(f"Reading file: {self._fileName}")
        print("Creating graph...")
        file = open(self._fileName)
        fileLines = file.readlines()
        count = 0
        filename_split = self._fileName.split('-')
        filename_split_by_dot = filename_split[2].split('.')

        density = filename_split_by_dot[0] + '.' + filename_split_by_dot[1]
        self._problemInfo.density = density
        for line in fileLines:
            if count == 0:
                self._problemInfo.nodes = int(line.strip().split()[1])
            elif count == 1:
                self._problemInfo.source = int(line.strip().split()[1])
            elif count == 2:
                self._problemInfo.sink = int(line.strip().split()[1])
            elif count == 3:
                self._problemInfo.arcs = int(line.strip().split()[1])
            else:
                strippedLine = line.strip().split(" ")
                i_val = int(strippedLine[0])
                j_val = int(strippedLine[1])
                if i_val == j_val:
                    continue
                i = Node(i_val)
                j = Node(j_val)
                arc = Arc(i, j, int(strippedLine[2]))
                self._graph.add_node(i)
                self._graph.add_node(j)
                self._graph.add_arc(arc)
            count += 1
        file.close()
        print(f"nodes: {self._problemInfo.nodes}")
        print(f"source: {self._problemInfo.source}")
        print(f"sink: {self._problemInfo.sink}")
        print(f"arcs: {self._problemInfo.arcs}")
        print(f"density: {self._problemInfo.density}")
        print("Graph created!")

    def get_problem_info(self):
        return self._problemInfo

    def get_graph(self):
        return self._graph

    def print_graph(self):
        self._graph.print_nodes()


class LPWriter:
    def __init__(self, problem_info, graph, destination="./") -> None:
        self._problemInfo = problem_info
        self._graph = graph
        self._destination = destination

    def _get_function(self, node, obj=False):
        ret = ""
        for incoming in node.get_incoming_arcs():
            sign = "-" if obj is True else "+"
            ret += f" {sign} {incoming.get_id()}"
        for outgoing in node.get_outgoing_arcs():
            sign = "+" if obj is True else "-"
            ret += f" {sign} {outgoing.get_id()}"
        if obj is False:
            ret += " = 0"
        return ret

    def create_lp_file(self):
        if self._destination == './':
            filename = f'model-{self._problemInfo.nodes}-{self._problemInfo.density}.lp'
        else:
            filename = f'{self._destination}/model-{self._problemInfo.nodes}-{self._problemInfo.density}.lp'
        file = open(filename, "w")
        file.write(f"Maximize\n")  # write objective function
        objectiveFunction = self._get_function(self._graph.get_node_from_value(self._problemInfo.source), True)
        file.write("    obj: " + objectiveFunction + "\n")  # write objective function

        file.write("\nSubject To\n")  # write subject to
        for node_key in self._graph.get_nodes():
            node = self._graph.get_node_from_value(node_key)
            if node_key != self._problemInfo.source and node_key != self._problemInfo.sink:
                var_name = f"c_{node_key}"
                file.write(f"    {var_name}: " + self._get_function(node) + "\n")

        file.write("\nBounds\n")  # write bounds
        for arc in self._graph.get_arcs():
            file.write(f"    0 <= {arc.get_id()} <= {arc.get_capacity()}\n")

        file.write("\nEnd\n")  # write end
        file.close()
        print(f"File '{filename}' created!")


