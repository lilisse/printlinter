# Standard imports
from sys import stderr


def toto():
    return 1 + 2


stderr.write(toto())
# <printlinter disable-next PPL004>
stderr.write(toto())
