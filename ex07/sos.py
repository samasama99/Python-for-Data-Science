#!/usr/bin/env python3
import sys


def encode_morse(text):
    """
    Encodes a string into Morse code.
    """
    NESTED_MORSE = {
        "A": ".-", "B": "-...",
        "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-",
        "L": ".-..", "M": "--", "N": "-.",
        "O": "---", "P": ".--.", "Q": "--.-",
        "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--",
        "X": "-..-", "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..",
        "9": "----.", " ": "/"
    }

    morse_output = []
    for char in text.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_output.append(NESTED_MORSE[char])

    return " ".join(morse_output)


def main():
    """
    Main function to handle arguments and print Morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        print(encode_morse(text))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
