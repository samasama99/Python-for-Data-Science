#!/usr/bin/env python3
import sys
import string


def count_chars(text):
    """
    Counts and displays the number of uppercase letters, lowercase letters,
    punctuation marks, spaces, and digits in the given string.
    """
    length = len(text)
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punctuation = sum(1 for char in text if char in string.punctuation)
    spaces = sum(1 for char in text if char.isspace())
    digits = sum(1 for char in text if char.isdigit())

    print(f"The text contains {length} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Main function to handle command-line arguments and input prompt.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            try:
                text = sys.stdin.readline()
                if not text:
                    return
            except EOFError:
                return

        count_chars(text)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
