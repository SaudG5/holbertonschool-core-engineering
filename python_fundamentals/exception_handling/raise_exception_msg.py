#!/usr/bin/env python3
def raise_exception_msg(message=""):
    try:
        undefined_variable
    except NameError:
        raise NameError(message)
