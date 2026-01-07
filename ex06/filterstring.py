#!/usr/bin/env python3
import sys


def main():
    """
    Accepts a string and an integer N.
    Outputs a list of words from the string that have a length greater than N.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        txt = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        result = [w for w in txt.split() if (lambda x: len(x) > n)(w)]

        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
