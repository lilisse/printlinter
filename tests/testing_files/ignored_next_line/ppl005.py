# Standard imports
from sys import stdout


def toto():
    return 1 + 2


stdout.writelines(toto())
# <printlinter disable-next PPL005>
stdout.writelines(toto())
