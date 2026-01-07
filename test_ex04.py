import subprocess

def run_test(args, expected_output, expected_stderr=""):
    cmd = ['python3', 'ex04/whatis.py'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    output = result.stdout.strip()
    stderr = result.stderr.strip()
    
    # Compare output
    if output == expected_output:
        print(f"✅ Args {args}: OK")
    else:
        print(f"❌ Args {args}: FAIL")
        print(f"   Expected: '{expected_output}'")
        print(f"   Got:      '{output}'")

def test_ex04():
    print("--- Testing Normal Cases ---")
    run_test(['14'], "I'm Even.")
    run_test(['-5'], "I'm Odd.")
    run_test(['0'], "I'm Even.")

    print("\n--- Testing Error Cases ---")
    # Case: No arguments -> Should produce no output (based on subject PDF example)
    run_test([], "")
    
    # Case: Too many arguments
    run_test(['13', '5'], "AssertionError: more than one argument is provided")
    
    # Case: Non-integer argument
    run_test(['Hi!'], "AssertionError: argument is not an integer")
    
    # Case: Mixed types
    run_test(['13', 'Hi'], "AssertionError: more than one argument is provided")

if __name__ == "__main__":
    test_ex04()
