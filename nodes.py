from arcs import Arc


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
