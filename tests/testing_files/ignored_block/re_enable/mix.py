# Standard imports
from pprint import pprint


def toto():
    return 1 + 2


# <printlinter disable PPL002>
pprint(toto())
pprint(toto() + toto())
# <printlinter disable PPL001>
print(toto())
print(toto() + toto())
# <printlinter enable PPL001>
# <printlinter enable PPL002>
