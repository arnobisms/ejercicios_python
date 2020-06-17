"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(primera_lista, segunda_lista):
    if len(primera_lista) > len(segunda_lista): return False
    for i in range(len(segunda_lista) - len(primera_lista) + 1):
        if primera_lista == segunda_lista[i:i + len(primera_lista)]:
            return True
    return False


def check_lists(primera_lista, segunda_lista):
    if primera_lista == segunda_lista: return EQUAL
    if sublist(primera_lista, segunda_lista): return SUBLIST
    if sublist(segunda_lista, primera_lista): return SUPERLIST
    return UNEQUAL
