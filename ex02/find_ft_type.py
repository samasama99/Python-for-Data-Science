#!/usr/bin/env python3

def all_thing_is_obj(object: any) -> int:
    t = type(object)
    if isinstance(object, str):
        print(f"{object} is in the kitchen : {t}")
    elif isinstance(object, (list, tuple, set, dict)):
        print(f"{t.__name__.capitalize()} : {t}")
    else:
        print("Type not Found")
    return 42
