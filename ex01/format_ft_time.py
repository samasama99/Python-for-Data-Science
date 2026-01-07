#!/usr/bin/env python3

import time
from datetime import datetime

timestamp = time.time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or "
      f"{timestamp:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
