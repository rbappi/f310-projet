import time


class Timer:

    def __init__(self):
        self._start = None
        self._end = None
        self._elapsed = None

    def start(self):
        self._start = time.perf_counter()

    def stop(self):
        self._end = time.perf_counter()
        self._elapsed = self._end - self._start

    def get_elapsed(self):
        return self._elapsed

    def print_elapsed(self):
        return f"{self._elapsed:0.4f} seconds"
