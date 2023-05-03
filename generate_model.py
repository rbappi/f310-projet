import sys
from lp_handler import LPWriter, FileReader


def create_lp_file(file, dest="./"):
    fl = FileReader(file)
    graph = fl.get_graph()
    problemInfo = fl.get_problem_info()
    lpWriter = LPWriter(problemInfo, graph, dest)
    lpWriter.create_lp_file()


if __name__ == "__main__":
    length = len(sys.argv)
    if length < 2:
        print("Usage: python3 generate_model.py <filename> [<destination>]")
        exit(1)
    filename = sys.argv[1]
    if length == 3:
        destination = sys.argv[2]
        create_lp_file(filename, destination)
    else:
        create_lp_file(filename)
