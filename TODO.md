<!-- markdownlint-disable-file MD041 -->

## Summary

- [Summary](#summary)
- [Next version](#next-version)
  - [Ignore block of code](#ignore-block-of-code)
  - [Ignore the next line](#ignore-the-next-line)
  - [Configuration](#configuration)
    - [Colorized output](#colorized-output)
    - [ignored\_files with regex](#ignored_files-with-regex)
  - [Tests](#tests)
    - [On big projects](#on-big-projects)
- [For the future](#for-the-future)
  - [Other libraries](#other-libraries)
  - [Configuration](#configuration-1)
    - [Add configuration option](#add-configuration-option)
    - [Add configuration in command line](#add-configuration-in-command-line)
  - [Translation](#translation)
  - [Tests](#tests-1)
    - [BDD tests](#bdd-tests)
  - [Documentation](#documentation)

## Next version

<!-- TODO: lien du millestone -->

### Ignore block of code

<!-- TODO: lien de l'issue -->

Add way to disable linter from a line X to a line Y for single error, library errors or
all errors.

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

### Ignore the next line

<!-- TODO: lien de l'issue -->

Add way to disable linter for the next line for single error, library errors or
all errors.

```python
# <py-printlinter disable-next PPL002>
```

### Configuration

#### Colorized output

<!-- TODO: lien de l'issue -->

Add option in configuration to enable or disable colorized output.

#### ignored_files with regex

<!-- TODO: lien de l'issue -->

Modify ignored_files option to manage regex.

```yml
ignored_files: [toto/toto.py, toto/*, toto/*.py]
```

### Tests

#### On big projects

<!-- TODO: lien de l'issue -->

Add tests on "big project" like py-linq-sql, django, etc...

## For the future

### Other libraries

- [ ] rich (100-199) <!-- TODO: lien de l'issue -->

<!-- markdownlint-disable-next-line MD024 -->
### Configuration

#### Add configuration option

- [ ] lang <!-- TODO: lien de l'issue -->
- [ ] ignored_folder <!-- TODO: lien de l'issue -->

#### Add configuration in command line

<!-- TODO: lien de l'issue -->

- [ ] target version
- [ ] ignored files
- [ ] ignored folder
- [ ] disabled rules
- [ ] lang
- [ ] colorized output

### Translation

Translate readme and changelog.

- [ ] italien <!-- TODO: lien de l'issue -->
- [ ] spanish <!-- TODO: lien de l'issue -->
- [ ] indian <!-- TODO: lien de l'issue -->
- [ ] chinese <!-- TODO: lien de l'issue -->

<!-- markdownlint-disable-next-line MD024 -->
### Tests

#### BDD tests

<!-- TODO: lien de l'issue -->

Add user tests with [pytest-bdd](https://github.com/pytest-dev/pytest-bdd).

### Documentation

- [ ] github pages <!-- TODO: lien de l'issue -->
- [ ] readthedoc <!-- TODO: lien de l'issue -->
