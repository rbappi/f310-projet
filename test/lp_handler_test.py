# tests all the instances from ../instances

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generate_model import main as gm



def main():
    for filename in os.listdir("instances"):
        if filename.endswith(".txt"):
            print(f"----------->Creating model for {filename}")
            gm(f"instances/{filename}", "results/lp")


if __name__ == "__main__":
    main()
