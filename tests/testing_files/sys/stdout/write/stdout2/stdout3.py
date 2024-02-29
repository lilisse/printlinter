# Standard imports
import sys
from sys import stdout


def titi():
    return 2


def toto():
    sys.stdout.write("toto")  # noqa: PPL003
    stdout.write("toto")  # noqa: PPL003
    sys.stdout.write("tata")
    stdout.write("tata")
    return 1
