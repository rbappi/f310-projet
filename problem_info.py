#!/usr/bin/python

class ProblemInfo:
    def __init__(self):
        self.__nodes = None
        self.__source = None
        self.__sink = None
        self.__arcs = None
        # pass

    def setAll(self, nodes, source, sink, arcs):
        self.__nodes = nodes
        self.__source = source
        self.__sink = sink
        self.__arcs = arcs

    @property
    def nodes(self):
        return self.__nodes

    @property
    def source(self):
        return self.__source

    @property
    def sink(self):
        return self.__sink

    @property
    def arcs(self):
        return self.__arcs

    @nodes.setter
    def nodes(self, nodes):
        self.__nodes = nodes

    @source.setter
    def source(self, source):
        self.__source = source

    @sink.setter
    def sink(self, sink):
        self.__sink = sink

    @arcs.setter
    def arcs(self, arcs):
        self.__arcs = arcs


