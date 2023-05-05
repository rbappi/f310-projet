class Node:
    def __init__(self, value):
        self._value = value
        self._incoming_arcs = []
        self._outgoing_arcs = []

    def add_outgoing_arc(self, arc):
        self._outgoing_arcs.append(arc)

    def add_incoming_arc(self, arc):
        self._incoming_arcs.append(arc)

    def __repr__(self):
        return f"Node({self._value})"

    def get_outgoing_arcs(self):
        return self._outgoing_arcs

    def get_incoming_arcs(self):
        return self._incoming_arcs

    def get_value(self):
        return self._value
