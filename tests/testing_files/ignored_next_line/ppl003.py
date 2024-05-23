# Standard imports
from sys import stdout


def toto():
    return 1 + 2


stdout.write(toto())
# <printlinter disable-next PPL003>
stdout.write(toto())
