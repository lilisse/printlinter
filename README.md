<!-- markdownlint-disable-file MD024 -->

# Py-printlinter

## TODO

### 0.1.0 - beta

#### Fix

- Need to be possible to launch lint on file and not only on folder

#### Add to rules

##### Standard

- [x] print <!-- PPL001 -->
- [x] pprint <!-- PPL002 -->
- [x] sys.stdout.write & stdout.write  <!-- PPL003 -->
- [x] sys.stderr.write & stderr.write <!-- PPL004 -->
- [x] sys.stdout.writelines & stdout.writelines <!-- PPL005 -->
- [x] sys.stderr.writelines & stderr.writelines <!-- PPL006 -->

#### Add more way to ignore

- [x] Inline
- [ ] All file

##### Inline

Ignore a rules (or all rules) on a line.

```python
toto = 1
titi = 2
print (toto + titi) # noqa: PPL001
```

##### All file

To ignore a rules on all one file.

```python
# <py-printlinter disable-file PPL001>
toto = 1
titi = 2
print(titi + toto)
# ...
```

To ignore all rules on all one file.

```python
# <py-printlinter disable-file ALL>
toto = 1
titi = 2
print(titi + toto)
# ...
```

To ignore all rules of one librairties on all one file.

- 0 for standrad [000-099]
- 1 for rich [100-199]

```python
# <py-printlinter disable-file PPL000>
toto = 1
titi = 2
print(titi + toto)
# ...
```

```python
# <py-printlinter disable-file PPL100>
toto = 1
titi = 2
rich.console.Console().print(titi + toto)
# ...
```

#### Add a LICENSE

- [x] LICENSE.md

#### Create a real README

- [ ] french
- [ ] english

#### Create a CHANGELOG

- [ ] french
- [ ] english

### Add configuration

- [ ] target version
- [ ] ignored files
- [ ] disabled rules
- [ ] enabled rules
- [ ] lang
- [ ] colorized output

In formats:

- [ ] toml
- [ ] json
- [ ] yaml
- [ ] pyproject

### Later

#### Add to rules

##### Rich (not for first beta version)

- [ ] rich.console.print <!-- PPL101 -->

#### Add more way to ignore

- [ ] a block of code

##### Block of code

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

#### Add configuration

- [ ] lang
- [ ] colorized output

#### Create a real README

- [ ] italien
- [ ] spanish
- [ ] indian
- [ ] chinese

#### Create a CHANGELOG

- [ ] italien
- [ ] spanish
- [ ] indian
- [ ] chinese

#### Add a good documentation

- [ ] Documentation on readthedoc

#### Add linter on pypi

- [ ] Add py-printlinter on pypi
