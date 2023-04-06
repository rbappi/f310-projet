#!/usr/bin/python
from problem_info import ProblemInfo
import linecache


class FileReader():
    def __init__(self, fileName) -> None:
        self._fileName = fileName
        self._problemInfo = ProblemInfo()
        self._readFile()

    def _readFile(self):
        file = open(self._fileName)
        fileLines = file.readlines()
        count = 0
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
                break
            count += 1
        file.close()
        print(f"nodes: {self._problemInfo.nodes}")
        print(f"source: {self._problemInfo.source}")
        print(f"sink: {self._problemInfo.sink}")
        print(f"arcs: {self._problemInfo.arcs}")




def main():
    FileReader("instances/inst-100-0.1.txt")



if __name__ == "__main__":
    main()
