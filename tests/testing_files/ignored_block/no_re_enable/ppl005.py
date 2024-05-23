# Standard imports
from sys import stdout


def toto():
    return 1 + 2


# <py-printlinter disable PPL005>
stdout.writelines(toto())
stdout.writelines(toto() + toto())
