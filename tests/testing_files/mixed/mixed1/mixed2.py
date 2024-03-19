# Standard imports
import sys
from pprint import pprint

print("toto")
pprint("titi")

print("tata")  # noqa: PPL001
pprint("tutu")  # noqa: PPL002
# fskof
print("foo")  # noqa: PPL002
pprint("bar")  # noqa: PPL001

abs(-1)
sys.stdin.read()

# fsiojfs
# fsopfs
