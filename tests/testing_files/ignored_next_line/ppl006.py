# Standard imports
from sys import stderr


def toto():
    return 1 + 2


stderr.writelines(toto())
# <py-printlinter disable-next PPL006>
stderr.writelines(toto())
