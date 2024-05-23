# Standard imports
from sys import stderr


def toto():
    return 1 + 2


# <printlinter disable PPL006>
stderr.writelines(toto())
stderr.writelines(toto() + toto())
# <printlinter enable PPL006>
