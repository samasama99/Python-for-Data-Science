#!/usr/bin/env python3

import sys

try:
    if len(sys.argv) < 2:
        sys.exit()

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    try:
        val = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if val % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")
