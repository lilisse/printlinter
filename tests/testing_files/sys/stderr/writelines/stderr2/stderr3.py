# Standard imports
import sys
from sys import stderr


def titi():
    return 2


def toto():
    sys.stderr.writelines(["toto", "titi"])  # noqa: PPL006
    stderr.writelines(["toto", "titi"])  # noqa: PPL006
    sys.stderr.writelines(["tata", "tutu"])
    stderr.writelines(["tata", "tutu"])
    return 1
