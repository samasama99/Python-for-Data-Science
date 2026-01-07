from ex03.NULL_not_found import NULL_not_found
import math

def test_ex03():
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False

    print("--- Testing Nothing ---")
    NULL_not_found(Nothing)

    print("\n--- Testing Garlic (NaN) ---")
    NULL_not_found(Garlic)

    print("\n--- Testing Zero ---")
    NULL_not_found(Zero)

    print("\n--- Testing Empty ---")
    NULL_not_found(Empty)

    print("\n--- Testing Fake ---")
    NULL_not_found(Fake)

    print("\n--- Testing Unknown (Brian) ---")
    ret = NULL_not_found("Brian")
    print(f"Return for unknown: {ret}")

if __name__ == "__main__":
    test_ex03()
