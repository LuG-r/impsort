import argparse
import os
from formatter import Formatter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="impSort",
        description="The python utility to organise your imports!",
        epilog="",
    )
    parser.add_argument(
        "source", help="Path to the file or directory you would like to organise."
    )
    parser.add_argument(
        "-p",
        "--preview",
        action="store_true",
        help="[NON FUNCTIONAL] Preview changes before any files are modified.",
    )
    parser.add_argument(
        "-c",
        "--check-semantic",
        action="store_true",
        help="[NON FUNCTIONAL] Ensure the modified code is semantically identical to source.",
    )
    args = parser.parse_args()
    if os.path.isdir(args.source):
        print(f"{args.source} is a directory")
        exit(0)

    f = Formatter()
    try:
        f.format_file(args.source)
    except ValueError as e:
        print(e)
