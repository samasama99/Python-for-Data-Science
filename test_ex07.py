import subprocess

def run_test(arg, expected, desc):
    cmd = ['python3', 'ex07/sos.py'] + arg
    res = subprocess.run(cmd, capture_output=True, text=True)
    out = res.stdout.strip()
    if out == expected:
        print(f"✅ {desc}: OK")
    else:
        print(f"❌ {desc}: FAIL")
        print(f"   Expected: {expected}")
        print(f"   Got:      {out}")

def test_ex07():
    print("--- Testing ex07/sos.py ---")
    
    # Normal Case: "SOS"
    # S=... O=--- S=... -> ... --- ...
    run_test(["SOS"], "... --- ...", "SOS Upper")
    
    # Normal Case: "sos" (Lower case check)
    run_test(["sos"], "... --- ...", "SOS Lower")
    
    # Space check: "h e" -> ".... / ."
    run_test(["h e"], ".... / .", "Space Handling")
    
    # Error: 0 args
    run_test([], "AssertionError: the arguments are bad", "No Args")
    
    # Error: 2 args
    run_test(["A", "B"], "AssertionError: the arguments are bad", "Too Many Args")
    
    # Error: Invalid Char ($)
    run_test(["h$ello"], "AssertionError: the arguments are bad", "Invalid Char")

if __name__ == "__main__":
    test_ex07()
