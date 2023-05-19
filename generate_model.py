import sys

from file_handler import LPWriter, FileReader


def main(file, dest="./"):
    fl = FileReader(file)
    graph = fl.get_graph()
    problemInfo = fl.get_problem_info()
    lpWriter = LPWriter(problemInfo, graph, dest)
    lpWriter.create_lp_file()


if __name__ == "__main__":
    length = len(sys.argv)
    if length < 2 or length > 3:
        print("Usage: python3 generate_model.py <filename> [<destination>]")
        exit(1)
    filename = sys.argv[1]
    if length == 3:
        destination = sys.argv[2]
        main(filename, destination)
    else:
        main(filename)
