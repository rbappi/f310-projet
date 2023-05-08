class Arc:
    def __init__(self, start_node, end_node, capacity=1):
        self._start_node = start_node
        self._end_node = end_node
        self._capacity = capacity
        self._id = f"x_{start_node.get_value()}_{end_node.get_value()}"

    def __repr__(self):
        return f"Arc(id: {self.id}, weight: {self._capacity})"

    def get_start_node(self):
        return self._start_node

    def get_end_node(self):
        return self._end_node

    def get_id(self):
        return self.id

    def get_capacity(self):
        return self._capacity

    @property
    def start_node(self):
        return self._start_node

    @property
    def end_node(self):
        return self._end_node

    @property
    def id(self):
        return self._id


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
