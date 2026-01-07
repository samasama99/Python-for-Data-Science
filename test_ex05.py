import subprocess

def run_test(args, expected_output, input_str=None):
    cmd = ['python3', 'ex05/building.py'] + args
    result = subprocess.run(cmd, input=input_str, capture_output=True, text=True)
    
    output = result.stdout.strip()
    
    # Check if all expected lines are present (partial matching might be safer for complex outputs)
    if all(line in output for line in expected_output):
        print(f"✅ Args {args}: OK")
    else:
        print(f"❌ Args {args}: FAIL")
        print(f"   Expected lines: {expected_output}")
        print(f"   Got output:\n{output}")

def test_ex05():
    print("--- Testing Normal Case (Argument) ---")
    # "Hello World!" passed as arg -> 12 chars
    expected = [
        "The text contains 12 characters:",
        "2 upper letters",
        "8 lower letters",
        "1 punctuation marks",
        "1 spaces",
        "0 digits"
    ]
    run_test(["Hello World!"], expected)

    print("\n--- Testing Error Case (More than 1 argument) ---")
    run_test(["Arg1", "Arg2"], ["AssertionError: more than one argument is provided"])

    print("\n--- Testing Input Prompt (No argument) ---")
    # Input: "Hello World!\n" -> 13 chars (Newline counts as space)
    # 2 Upper, 8 Lower, 1 Punc, 2 Spaces (1 space + 1 newline), 0 Digits
    expected_prompt = [
        "What is the text to count?",
        "The text contains 13 characters:",
        "2 upper letters",
        "8 lower letters",
        "1 punctuation marks",
        "2 spaces",
        "0 digits"
    ]
    run_test([], expected_prompt, input_str="Hello World!\n")

if __name__ == "__main__":
    test_ex05()