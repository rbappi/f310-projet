# tests all the instances from ../instances

import os
from generate_model import create_lp_file


def main():
    for filename in os.listdir("../instances"):
        if filename.endswith(".txt"):
            print(f"----------->Creating model for {filename}")
            create_lp_file(f"../instances/{filename}", "../test/instance_output")


if __name__ == "__main__":
    main()
