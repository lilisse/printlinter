# Standard imports
from pprint import pprint
from sys import stderr, stdout


def toto():
    return 1 + 2


# <py-printlinter disable ALL>
print(toto())
pprint(toto())
stdout.write(toto())
stderr.write(toto())
stdout.writelines(toto())
stderr.writelines(toto())
