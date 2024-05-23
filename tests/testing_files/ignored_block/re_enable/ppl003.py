# Standard imports
from sys import stdout


def toto():
    return 1 + 2


# <printlinter disable PPL003>
stdout.write(toto())
stdout.write(toto() + toto())
# <printlinter enable PPL003>
