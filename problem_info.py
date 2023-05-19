#!/usr/bin/python

class ProblemInfo:
    def __init__(self):
        self._nodes = None
        self._source = None
        self._sink = None
        self._arcs = None
        self._density = None
        # pass

    def setAll(self, nodes, source, sink, arcs, density):
        self._nodes = nodes
        self._source = source
        self._sink = sink
        self._arcs = arcs
        self._density = density

    @property
    def nodes(self):
        return self._nodes

    @property
    def source(self):
        return self._source

    @property
    def sink(self):
        return self._sink

    @property
    def arcs(self):
        return self._arcs

    @nodes.setter
    def nodes(self, nodes):
        self._nodes = nodes

    @source.setter
    def source(self, source):
        self._source = source

    @sink.setter
    def sink(self, sink):
        self._sink = sink

    @arcs.setter
    def arcs(self, arcs):
        self._arcs = arcs

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, density):
        self._density = density
