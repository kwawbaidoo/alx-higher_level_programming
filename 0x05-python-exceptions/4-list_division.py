#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    takes two lists and creates a new list with result of divison
    operation
    handles errors and prints them to stdout
    """
    i = 0
    new_list = []
    ans = 0
    for i in range(0, list_length):
        try:
            ans = (my_list_1[i] / my_list_2[i])
        except TypeError:
            ans = 0
            print("wrong type")
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        except IndexError:
            ans = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
