# Standard imports
import sys
from pprint import pprint
from sys import stderr, stdout

# <printlinter disable-file ALL>

print("toto")

pprint("toto")

sys.stdout.write("toto")
stdout.write("toto")

sys.stderr.write("toto")
stderr.write("toto")

sys.stdout.writelines("toto")
stdout.writelines("toto")

sys.stderr.writelines("toto")
stderr.writelines("toto")
