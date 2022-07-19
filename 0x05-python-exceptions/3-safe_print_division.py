#!/usr/bin/python3


def safe_print_division(a, b):
    """
    divides two integers and prints the result
    catches divide by zero exception
    """
    try:
        ans = a / b
    except ZeroDivisionError:
        ans = None
    finally:
        print("Inside result: {}".format(ans))
    return ans
