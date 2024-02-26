# Standard imports
from pprint import pprint

print("toto")
pprint("titi")

print("tata")  # noqa: PPL001
pprint("tutu")  # noqa: PPL002

print("foo")  # noqa: PPL002
pprint("bar")  # noqa: PPL001

abs(-1)
