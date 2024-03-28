<!-- markdownlint-disable-file MD041 -->

Todo list of the project.

## Summary

- [Summary](#summary)
- [Next version](#next-version)
  - [Ignore block of code](#ignore-block-of-code)
  - [Ignore the next line](#ignore-the-next-line)
  - [Configuration](#configuration)
    - [Colorized output](#colorized-output)
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

[Version 0.2.0](https://github.com/lilisse/printlinter/milestone/1)

### Ignore block of code

[Issue](https://github.com/lilisse/printlinter/issues/5)

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

[Issue](https://github.com/lilisse/printlinter/issues/1)

Add way to disable linter for the next line for single error, library errors or
all errors.

```python
# <py-printlinter disable-next PPL002>
```

### Configuration

#### Colorized output

[Issue](https://github.com/lilisse/printlinter/issues/6)

Add option in configuration to enable or disable colorized output.

### Tests

#### On big projects

[Issue](https://github.com/lilisse/printlinter/issues/7)

Add tests on "big project" like py-linq-sql, django, etc...

## For the future

### Other libraries

- [ ] rich (100-199) [Issue](https://github.com/lilisse/printlinter/issues/8)

<!-- markdownlint-disable-next-line MD024 -->
### Configuration

#### Add configuration option

- [ ] lang [Issue](https://github.com/lilisse/printlinter/issues/9)
- [ ] ignored_file_with_regex [Issue](https://github.com/lilisse/printlinter/issues/10)

#### Add configuration in command line

[Issue](https://github.com/lilisse/printlinter/issues/11)

- [ ] target version
- [ ] ignored files
- [ ] disabled rules
- [ ] lang
- [ ] colorized output

### Translation

Translate README.md and CHANGELOG.md.

- [ ] italian [Issue](https://github.com/lilisse/printlinter/issues/12)
- [ ] deutsche [Issue](https://github.com/lilisse/printlinter/issues/13)
- [ ] portuguese [Issue](https://github.com/lilisse/printlinter/issues/14)
- [ ] japanese [Issue](https://github.com/lilisse/printlinter/issues/15)
- [ ] korean [Issue](https://github.com/lilisse/printlinter/issues/16)
- [ ] spanish [Issue](https://github.com/lilisse/printlinter/issues/17)
- [ ] indian [Issue](https://github.com/lilisse/printlinter/issues/18)
- [ ] chinese [Issue](https://github.com/lilisse/printlinter/issues/19)

<!-- markdownlint-disable-next-line MD024 -->
### Tests

#### BDD tests

[Issue](https://github.com/lilisse/printlinter/issues/20)

Add user tests with [pytest-bdd](https://github.com/pytest-dev/pytest-bdd).

### Documentation

- [ ] github pages
- [ ] readthedoc
