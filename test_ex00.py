import subprocess
import ast

def test_ex00():
    try:
        # Run the student's script
        result = subprocess.run(['python3', 'ex00/Hello.py'], capture_output=True, text=True)
        output = result.stdout.strip().split('\n')

        if len(output) != 4:
            print("❌ Error: Expected 4 lines of output.")
            return

        # 1. Validate List
        try:
            lst = ast.literal_eval(output[0])
            if not isinstance(lst, list):
                print(f"❌ Error: Line 1 should be a list. Got {type(lst)}")
            elif lst != ['Hello', 'World!']:
                print(f"❌ Error: List output incorrect. Expected ['Hello', 'World!'], got {lst}")
            else:
                print("✅ List: OK")
        except:
            print(f"❌ Error: Could not parse line 1 as a list: {output[0]}")

        # 2. Validate Tuple
        try:
            tup = ast.literal_eval(output[1])
            if not isinstance(tup, tuple):
                print(f"❌ Error: Line 2 should be a tuple. Got {type(tup)}")
            elif len(tup) != 2 or tup[0] != "Hello":
                 print(f"❌ Error: Tuple format incorrect. Got {tup}")
            else:
                print(f"✅ Tuple: OK (Country: {tup[1]})")
        except:
            print(f"❌ Error: Could not parse line 2 as a tuple: {output[1]}")

        # 3. Validate Set
        try:
            st = ast.literal_eval(output[2])
            if not isinstance(st, set):
                # Empty set prints as set(), but here we expect elements
                print(f"❌ Error: Line 3 should be a set. Got {type(st)}")
            elif "Hello" not in st or len(st) != 2:
                print(f"❌ Error: Set should contain 'Hello' and one other element. Got {st}")
            else:
                city = list(st - {"Hello"})[0]
                print(f"✅ Set: OK (City: {city})")
        except:
            print(f"❌ Error: Could not parse line 3 as a set: {output[2]}")

        # 4. Validate Dict
        try:
            dct = ast.literal_eval(output[3])
            if not isinstance(dct, dict):
                print(f"❌ Error: Line 4 should be a dict. Got {type(dct)}")
            elif "Hello" not in dct:
                print(f"❌ Error: Dict should have key 'Hello'. Got {dct}")
            elif not isinstance(dct["Hello"], str):
                 print(f"❌ Error: Dict value should be a string, got {type(dct['Hello'])}. Content: {dct['Hello']}")
            else:
                print(f"✅ Dict: OK (Campus: {dct['Hello']})")
        except:
             print(f"❌ Error: Could not parse line 4 as a dict: {output[3]}")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_ex00()
