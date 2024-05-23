# Standard imports
from pprint import pprint


def toto():
    return 1 + 2


# <printlinter disable PPL002>
pprint(toto())
pprint(toto() + toto())
# <printlinter enable PPL002>
