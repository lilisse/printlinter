# Standard imports
from pprint import pprint


def toto():
    return 1 + 2


# <py-printlinter disable PPL002>
pprint(toto())
pprint(toto() + toto())
# <py-printlinter disable PPL001>
print(toto())
print(toto() + toto())
# <py-printlinter enable PPL001>
# <py-printlinter enable PPL002>
