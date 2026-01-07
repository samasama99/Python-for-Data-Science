import subprocess
import re
import time
from datetime import datetime

def test_ex01():
    try:
        # Run the student's script
        result = subprocess.run(['python3', 'ex01/format_ft_time.py'], capture_output=True, text=True)
        output = result.stdout.strip().split('\n')

        if len(output) != 2:
            print(f"❌ Error: Expected 2 lines of output, got {len(output)}.")
            print("Output was:")
            for line in output:
                print(line)
            return

        # Line 1 Check
        # Expected: Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
        line1 = output[0]
        pattern1 = r"^Seconds since January 1, 1970: ([0-9,]+\.[0-9]+) or ([0-9]\.[0-9]{2}e\+[0-9]{2}) in scientific notation$?$"
        match1 = re.match(pattern1, line1)
        
        if not match1:
            print("❌ Error: Line 1 format is incorrect.")
            print(f"Got: {line1}")
            print("Expected format: Seconds since January 1, 1970: <number_with_commas> or <sci_notation> in scientific notation")
        else:
            # Check if values are consistent
            str_val = match1.group(1).replace(',', '')
            sci_val = match1.group(2)
            try:
                val = float(str_val)
                current_time = time.time()
                if abs(val - current_time) > 86400: # Allow 1 day drift just in case, but really should be close
                    print(f"⚠️ Warning: Timestamp {val} seems far from now ({current_time}). Check your calculation.")
                else:
                    print("✅ Line 1: Format and Value look good.")
            except ValueError:
                print("❌ Error: Could not parse numbers in Line 1.")

        # Line 2 Check
        # Expected: Oct 21 2022
        line2 = output[1]
        try:
            # Try parsing with strptime to validate format
            # Using clean format matches: "%b %d %Y"
            # Remove potential trailing $ if user hardcoded it from subject
            clean_line2 = line2.rstrip('$')
            dt = datetime.strptime(clean_line2, "%b %d %Y")
            print(f"✅ Line 2: Date format OK ({clean_line2})")
        except ValueError:
            print("❌ Error: Line 2 format is incorrect.")
            print(f"Got: {line2}")
            print("Expected format: Month Day Year (e.g., Jan 01 1970)")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_ex01()
