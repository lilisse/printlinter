# Standard imports
from sys import stderr


def toto():
    return 1 + 2


# <printlinter disable PPL004>
stderr.write(toto())
stderr.write(toto() + toto())
# <printlinter enable PPL004>
