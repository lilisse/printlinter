# Standard imports
import sys
from sys import stdout


def titi():
    return 2


def toto():
    sys.stdout.writelines(["toto", "titi"])  # noqa: PPL005
    stdout.writelines(["toto", "titi"])  # noqa: PPL005
    sys.stdout.writelines(["tata", "tutu"])
    stdout.writelines(["tata", "tutu"])
    return 1
