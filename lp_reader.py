#!/usr/bin/python
# from arcs import Arc
# from nodes import Node
from problem_info import ProblemInfo
# from graph import Graph, Node, Arc
# from test import Graph, Node, Edge
from directedGraph2 import DirectedGraph, Node, Arc
import linecache
import sys



class FileReader():
    def __init__(self, fileName) -> None:
        self._fileName = fileName
        self._problemInfo = ProblemInfo()
        self._graph = DirectedGraph()
        # self._readFile()


    def _readFile(self):
        nodesAlreadyRead = []
        file = open(self._fileName)
        fileLines = file.readlines()
        count = 0
        filenameSplitted = self._fileName.split('-')
        unsterilisedDensity = filenameSplitted[2].split('.')
        density = unsterilisedDensity[0] + '.' + unsterilisedDensity[1]
        self._problemInfo.density = density
        for line in fileLines:
            if count == 0:
                self._problemInfo.nodes = line.strip().split()[1]
            elif count == 1:
                self._problemInfo.source = line.strip().split()[1]
            elif count == 2:
                self._problemInfo.sink = line.strip().split()[1]
            elif count == 3:
                self._problemInfo.arcs = line.strip().split()[1]
            else:
                strippedLine = line.strip().split(" ")
                i_val = int(strippedLine[0])
                j_val = int(strippedLine[1])
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

    def getProblemInfo(self):
        return self._problemInfo

    def getGraph(self):
        # print(f"graph: {self._graph.getGraph()}")
        self._graph.get_nodes()
        # print(f"edges: {self._graph.get_edges()}")
        # return self._graph.get_nodes()


class LPWriter():
    def __init__(self, problemInfo) -> None:
        self._problemInfo = problemInfo
        self._createLPFile()

    def _createLPFile(self):
        file = open(f'model-{self._problemInfo.nodes}-{self._problemInfo.density}', 'w')
        file.write(f"Maximze\nobj: ") # write objective function
        for i in range(1, int(self._problemInfo.nodes) + 1):
            if i == int(self._problemInfo.nodes):
                file.write(f"x{i}")
            else:
                file.write(f"x{i} + ")
        file.close()




def main():
    # fl = FileReader("instances/inst-100-0.1.txt")
    fl = FileReader("instances/inst-1500-0.3.txt")
    fl._readFile()
    fl.getGraph()



if __name__ == "__main__":
    main()
