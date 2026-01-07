#!/usr/bin/env python3

import math


def NULL_not_found(object: any) -> int:
    t = type(object)
    if object is None:
        print(f"Nothing: {object} {t}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan {t}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {t}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {t}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {t}")
    else:
        print("Type not Found")
        return 1
    return 0
