from ex02.find_ft_type import all_thing_is_obj

def test_ex02():
    print("--- Testing List ---")
    ret = all_thing_is_obj(["Hello", "tata!"])
    print(f"Return: {ret}")

    print("\n--- Testing Tuple ---")
    ret = all_thing_is_obj(("Hello", "toto!"))
    print(f"Return: {ret}")

    print("\n--- Testing Set ---")
    ret = all_thing_is_obj({"Hello", "tutu!"})
    print(f"Return: {ret}")

    print("\n--- Testing Dict ---")
    ret = all_thing_is_obj({"Hello": "titi!"})
    print(f"Return: {ret}")

    print("\n--- Testing String (Brian) ---")
    ret = all_thing_is_obj("Brian")
    print(f"Return: {ret}")

    print("\n--- Testing String (Toto) ---")
    ret = all_thing_is_obj("Toto")
    print(f"Return: {ret}")

    print("\n--- Testing Unknown Type (Int) ---")
    ret = all_thing_is_obj(10)
    print(f"Return: {ret}")

if __name__ == "__main__":
    test_ex02()
