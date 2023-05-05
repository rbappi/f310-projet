from directed_graph import DirectedGraph
from arc import Arc
from node import Node


class ArcWithFlow(Arc):
    def __init__(self, i, j, capacity=0, flow=0) -> None:
        super().__init__(i, j, capacity)
        self._flow = flow

    def get_flow(self):
        return self._flow

    def set_flow(self, flow):
        self._flow = flow

    def __repr__(self):
        return f"Arc(id: {self.id}, weight: {self._capacity}, flow: {self._flow})"
