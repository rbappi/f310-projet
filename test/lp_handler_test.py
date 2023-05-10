# tests all the instances from ../instances

import os
from generate_model import main


def main():
    for filename in os.listdir("../instances"):
        if filename.endswith(".txt"):
            print(f"----------->Creating model for {filename}")
            main(f"../instances/{filename}", "../test/instance_output")


if __name__ == "__main__":
    main()
