# Standard imports
from sys import stdout


def toto():
    return 1 + 2


stdout.writelines(toto())
# <py-printlinter disable-next PPL005>
stdout.writelines(toto())
