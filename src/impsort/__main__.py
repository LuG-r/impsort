import argparse
import os
from formatter import Formatter


def main():
    parser = argparse.ArgumentParser(
        prog="impsort",
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

    try:
        f = Formatter()
        if os.path.isdir(args.source):
            f.format_directory(args.source)
        else:
            f.format_file(args.source)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
