import sys
from timer import Timer
from file_handler import FileReader
from chemin_augmentant_processor import CheminAugmentant


def main(file, dest="./"):
    timer = Timer()
    fl = FileReader(file)
    graph = fl.get_graph()
    problem_info = fl.get_problem_info()
    if dest == './':
        file_sol = f"model-{problem_info.nodes}-{problem_info.density}.path"
    else:
        file_sol = f"{dest}/model-{problem_info.nodes}-{problem_info.density}.path"
    chemin_augmentant = CheminAugmentant(graph, problem_info)
    print("---------------------------------")
    print("Running chemin augmentant...")
    timer.start()
    chemin_augmentant.chemin_augmentant(graph, problem_info)
    max_flow = chemin_augmentant.get_max_flow()
    timer.stop()
    print(f"Resolution complete in {timer.print_elapsed()}.")
    print(f"Max flow from source calculated: {max_flow}")
    arcs = chemin_augmentant.get_arcs()
    file_to_write = open(file_sol, "w")
    print(f"Writing solution to '{file_sol}'...")
    file_to_write.write(f"Max flow from source calculated: {max_flow}\n")
    file_to_write.write(f"Resolution complete in {timer.print_elapsed()}.\n")
    for arc in arcs:
        file_to_write.write(f"{arcs[arc]}\n")
    file_to_write.close()
    print("Done!")
    return timer.get_elapsed()


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