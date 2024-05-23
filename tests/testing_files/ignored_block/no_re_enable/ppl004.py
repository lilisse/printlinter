# Standard imports
from sys import stderr


def toto():
    return 1 + 2


# <py-printlinter disable PPL004>
stderr.write(toto())
stderr.write(toto() + toto())
