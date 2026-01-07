from ex06.ft_filter import ft_filter
import subprocess

def test_ft_filter():
    print("--- Testing ft_filter vs filter ---")
    
    # Test 1: Even numbers
    nums = [1, 2, 3, 4, 5, 6]
    is_even = lambda x: x % 2 == 0
    
    # We convert to list to compare the output values
    # because ft_filter (now a generator) and filter (iterator) don't equal each other directly
    my_res = list(ft_filter(is_even, nums))
    py_res = list(filter(is_even, nums))
    
    if my_res == py_res:
        print(f"✅ Even Numbers: {my_res}")
    else:
        print(f"❌ Even Numbers: Expected {py_res}, got {my_res}")

    # Test 2: None function (truthy check)
    vals = [0, 1, False, True, "", "Hello", None]
    my_res = list(ft_filter(None, vals))
    py_res = list(filter(None, vals))
    
    if my_res == py_res:
        print(f"✅ None Function: {my_res}")
    else:
        print(f"❌ None Function: Expected {py_res}, got {my_res}")
        
    # Test 3: Docstring
    if ft_filter.__doc__ == filter.__doc__:
         print("✅ Docstring matches exactly.")
    else:
         print("⚠️ Docstring mismatch (Check indentation/content).")
         # print(f"Yours:\n{ft_filter.__doc__}\nOrigin:\n{filter.__doc__}")

def test_filterstring():
    print("\n--- Testing filterstring.py ---")
    
    def run_prog(args, expected, desc):
        cmd = ['python3', 'ex06/filterstring.py'] + args
        res = subprocess.run(cmd, capture_output=True, text=True)
        out = res.stdout.strip()
        if out == expected:
            print(f"✅ {desc}: OK")
        else:
            print(f"❌ {desc}: FAIL")
            print(f"   Expected: {expected}")
            print(f"   Got:      {out}")

    run_prog(["Hello the World", "4"], "['Hello', 'World']", "Normal Case")
    run_prog(["Hello the World", "99"], "[]", "Empty Result")
    run_prog(["3", "Hello the World"], "AssertionError: the arguments are bad", "Wrong Order")
    run_prog([], "AssertionError: the arguments are bad", "No Args")

if __name__ == "__main__":
    test_ft_filter()
    test_filterstring()
