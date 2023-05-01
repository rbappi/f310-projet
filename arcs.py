from nodes import Node


class Arc:

    def __init__(self, start: Node, end: Node, weight: int):
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
