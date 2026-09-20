#!/usr/bin/env python3
def raise_exception():
    none = None
    try:
        print("{:d}".format(none))
    except TypeError:
        pass
