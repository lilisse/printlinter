# Py-printlinter

## TODO

### Add to rules

#### Standard

- [x] print <!-- PPL001 -->
- [ ] pprint <!-- PPL002 -->
- [ ] sys.stdout.write <!-- PPL003 -->
- [ ] sys.stderr.write <!-- PPL004 -->

#### Rich

- [ ] rich.console.print <!-- PPL101 -->

### Add more way to ignore

- [x] Inline
- [ ] All file
- [ ] a block of code

#### Inline

Ignore a rules (or all rules) on a line.

```python
toto = 1
titi = 2
print (toto + titi) # noqa: PPL001
```

#### All file

To ignore a rules on all one file.

```python
# <py-printlinter file disable PPL001>
toto = 1
titi = 2
print(titi + toto)
# ...
```

To ignore all rules on all one file.

```python
# <py-printlinter file disable ALL>
toto = 1
titi = 2
print(titi + toto)
# ...
```

To ignore all rules of one librairties on all one file.

- 0 for standrad [000-099]
- 1 for rich [100-199]

```python
# <py-printlinter file disable PPL000>
toto = 1
titi = 2
print(titi + toto)
# ...
```

```python
# <py-printlinter file disable PPL100>
toto = 1
titi = 2
rich.console.Console().print(titi + toto)
# ...
```

#### Block of code

Block ignore is way to disable linter from a line X to a line Y.

```python
toto = 1
titi = 2
# <py-printlinter disable PPL001>
print(toto)
print(titi)
print (toto + titi)
# <py-printlinter enable PPL001>
```

All rules can be ignored.

```python
# <py-printlinter disable ALL>
```

And re enable.

```python
# <py-printlinter enable ALL>
```

For future, when we take other libraries than the standard one, we want ignore one
librairie. Each librairie had am hundred in error code.

- 0 for standrad [000-099]
- 1 for rich [100-199]

```python
toto = 1
titi = 2
# <py-printlinter disable PPL000>
print(toto)
print(titi)
print (toto + titi)
# <py-printlinter enable PPL000>
```

```python
toto = 1
titi = 2
# <py-printlinter disable PPL100>
print(toto)
print(titi)
rich.console.Console().print(toto + titi)
# <py-printlinter enable PPL100>
```

### Add configuration

- [ ] ignored files
- [ ] disabled rules
- [ ] enabled rules
- [ ] lang

In formats:

- [ ] toml
- [ ] json
- [ ] yaml
- [ ] pyproject

### Create a real README

- [ ] french
- [ ] english
- [ ] italien
- [ ] spanish
- [ ] indian
- [ ] chinese
- and more

### Create a CHANGELOG

- [ ] french
- [ ] english
- [ ] italien
- [ ] spanish
- [ ] indian
- [ ] chinese
- and more

### Add a LICENCE

- [ ] LICENCE.md

### Add a good documentation

- [ ] Documentation on readthedoc

### Add linter on pypi

- [ ] Add py-printlinter on pypi
