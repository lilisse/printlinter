# Standard imports
from pprint import pprint


def titi():
    return 2


def toto():
    pprint("toto")  # noqa: PPL002
    pprint("tata")
    return 1
