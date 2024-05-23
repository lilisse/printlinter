# Standard imports
from sys import stderr


def toto():
    return 1 + 2


# <py-printlinter disable PPL006>
stderr.writelines(toto())
stderr.writelines(toto() + toto())
# <py-printlinter enable PPL006>
