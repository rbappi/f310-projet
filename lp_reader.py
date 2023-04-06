#!/usr/bin/python
from problem_info import ProblemInfo


class FileReader():
    def __init__(self, fileName) -> None:
        self.fileName = fileName

    def readFile(self):
        nodes = 0
        source = 0
        sink = 99
        arcs = 961
        file = open(self.fileName)
        # for line in range(4):
        #     if line


def main():
    probI = ProblemInfo()
    probI.setAll(0, 0, 99, 961)
    # probI.arcs = 961
    print(probI.arcs)
    print("test")


if __name__ == "__main__":
    main()
