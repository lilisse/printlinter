# Standard imports
from sys import stdout


def toto():
    return 1 + 2


# <py-printlinter disable PPL003>
stdout.write(toto())
stdout.write(toto() + toto())
