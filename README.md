<!-- markdownlint-disable-file MD041 -->

<!-- TODO: Add badge -->
![logo](logo.png)

[English readme](README.md) **·** [Français readme](doc/readme/README.fr.md)

PrintLinter is a python linter to detect and signals display functions in python code.

## Summary

- [Installing](#installing)
- [Usage](#usage)
  - [Verbs](#verbs)
    - [Lint](#lint)
      - [Example](#example)
- [Error codes](#error-codes)
  - [Standard library](#standard-library)
- [Ignore errors](#ignore-errors)
  - [Ignore error inline](#ignore-error-inline)
    - [Examples](#examples)
  - [Ignore error on the next line](#ignore-error-on-the-next-line)
    - [Examples](#examples-1)
  - [Ignore a whole file](#ignore-a-whole-file)
    - [Examples](#examples-2)
      - [Simple error](#simple-error)
      - [library errors](#library-errors)
      - [All errors](#all-errors)
  - [Ignore a block of code](#ignore-a-block-of-code)
    - [Examples](#examples-3)
      - [Simple error](#simple-error-1)
      - [All errors](#all-errors-1)
- [Configuration](#configuration)
  - [Target version](#target-version)
  - [Ignored files](#ignored-files)
  - [Disabled rules](#disabled-rules)
  - [Color](#color)
  - [Examples of configuration files](#examples-of-configuration-files)
    - [Yaml/Yml configuration file](#yamlyml-configuration-file)
    - [Json configuration file](#json-configuration-file)
    - [Toml configuration file](#toml-configuration-file)
    - [Pyproject configuration file](#pyproject-configuration-file)
- [But then](#but-then)

# Installing

Install with `pip` or your favorite PyPI package manageer.

```sh
pip install printlinter
```

Run the following command to test PrintLinter.

```sh
printlinter --version
```

# Usage

## Verbs

For help on using a verb.

```sh
printlinter <verb> --help
```

### Lint

To lint a file or a folder.

```sh
printlinter lint <file|folder>
```

The product output look like this.

`file_path:line:column error_code display_function_detected error_name`

By default we disable the linter in some folders.

- `node_modules`
- `.vscode/`
- `__pycache__/`
- `build/`
- `develop-eggs/`
- `dist/`
- `downloads/`
- `eggs/`
- `.eggs/`
- `lib/`
- `lib64/`
- `parts/`
- `sdist/`
- `var/`
- `wheels/`
- `pip-wheel-metadata/`
- `share/python-wheels/`
- `htmlcov/`
- `.tox/`
- `.nox/`
- `.hypothesis/`
- `.pytest_cache/`
- `docs/_build/`
- `__pypackages__/`
- `.mypy_cache/`
- `.ruff_cache`
- `.pyre/`
- `env/`
- `venv/`
- `ENV/`
- `env.bak/`
- `venv.bak/`
- `.venv/`
- `.env/`

#### Example

<!-- markdownlint-disable MD013 -->
```sh
tests/testing_files/mixed/mixed0.py:5:0: PPL001 `print("toto")` print-detected
tests/testing_files/mixed/mixed0.py:6:0: PPL002 `pprint("titi")` prettyprint-detected
tests/testing_files/mixed/mixed1/mixed2.py:5:0: PPL001 `print("toto")` print-detected
tests/testing_files/mixed/mixed1/mixed2.py:6:0: PPL002 `pprint("titi")` prettyprint-detected
tests/testing_files/pprint/pprint1.py:6:0: PPL002 `pprint("Hello, world")` prettyprint-detected
tests/testing_files/pprint/pprint2/pprint3.py:11:4: PPL002 `pprint("tata")` prettyprint-detected
tests/testing_files/ignored_files/ignore_ppl005.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_nothing.py:6:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_nothing.py:8:0: PPL002 `pprint("toto")` prettyprint-detected
tests/testing_files/ignored_files/ignore_ppl006.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_ppl002.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_ppl001.py:9:0: PPL002 `pprint("toto")` prettyprint-detected
tests/testing_files/ignored_files/ignore_ppl004.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/ignore_ppl003.py:7:0: PPL001 `print("toto")` print-detected
tests/testing_files/ignored_files/disable_in_wrong_place.py:8:0: PPL001 `print("toto")` print-detected
tests/testing_files/sys/stderr/write/stderr1.py:7:0: PPL004 `sys.stderr.write("Hello, world")` sys.stderr.write-detected
tests/testing_files/sys/stderr/write/stderr1.py:8:0: PPL004 `stderr.write("Hello, world")` sys.stderr.write-detected
tests/testing_files/sys/stderr/write/stderr2/stderr3.py:13:4: PPL004 `sys.stderr.write("tata")` sys.stderr.write-detected
tests/testing_files/sys/stderr/write/stderr2/stderr3.py:14:4: PPL004 `stderr.write("tata")` sys.stderr.write-detected
tests/testing_files/sys/stderr/writelines/stderr1.py:7:0: PPL006 `sys.stderr.writelines(["Hello", "world"])` sys.stderr.writelines-detected
tests/testing_files/sys/stderr/writelines/stderr1.py:8:0: PPL006 `stderr.writelines(["Hello", "world"])` sys.stderr.writelines-detected
tests/testing_files/sys/stderr/writelines/stderr2/stderr3.py:13:4: PPL006 `sys.stderr.writelines(["tata", "tutu"])`
sys.stderr.writelines-detected
tests/testing_files/sys/stderr/writelines/stderr2/stderr3.py:14:4: PPL006 `stderr.writelines(["tata", "tutu"])`
sys.stderr.writelines-detected
tests/testing_files/sys/stdout/write/stdout1.py:7:0: PPL003 `sys.stdout.write("Hello, world")` sys.stdout.write-detected
tests/testing_files/sys/stdout/write/stdout2/stdout3.py:13:4: PPL003 `sys.stdout.write("tata")` sys.stdout.write-detected
tests/testing_files/sys/stdout/writelines/stdout1.py:7:0: PPL005 `sys.stdout.writelines(["Hello", "world"])` sys.stdout.writelines-detected
tests/testing_files/sys/stdout/writelines/stdout2/stdout3.py:14:4: PPL005 `stdout.writelines(["tata", "tutu"])`
sys.stdout.writelines-detected
tests/testing_files/print/toto_1.py:3:0: PPL001 `print("Hello, world")` print-detected
tests/testing_files/print/toto2/toto3.py:7:4: PPL001 `print("tata")` print-detected
Found 27 errors
```
<!-- markdownlint-enable MD013 -->

# Error codes

All errors have an individual code based on `PPLXXX`.
Each library have its own error "domain".

| Library  | Error domain |
|:---------|:-------------|
| Standard | PPL0XX       |

## Standard library

| Function                | Error code |
|:------------------------|:-----------|
| `print`                 | PPL001     |
| `pprint`                | PPL002     |
| `sys.stdout.write`      | PPL003     |
| `sys.stderr.write`      | PPL004     |
| `sys.stdout.writelines` | PPL005     |
| `sys.stderr.writelines` | PPL006     |

# Ignore errors

You can ignore errors with the linter.

## Ignore error inline

To ignore a rule inline, add a comment at the end of the line. `# noqa: <error_code>`.

### Examples

```python
toto = 1
titi = 2
print (toto + titi) # noqa: PPL001
```

## Ignore error on the next line

To ignore a rule on the next line, add a comment at the line before code to ignore.
`<printlinter disable-next (error_code)>`.

<!-- markdownlint-disable-next-line MD024 -->
### Examples

```python
toto = 1
titi = 2
# <printlinter disable-next PPL001>
print (toto + titi) # ignored error
```

## Ignore a whole file

To ignore a rule, library rules or all rules, add a comment at the beging of the file.
`# <printlinter disable-file (error_code)>`.

<!-- markdownlint-disable-next-line MD036 -->
**The comment must be before any code in a file.**

<!-- markdownlint-disable-next-line MD024 -->
### Examples

#### Simple error

```python
# <printlinter disable-file PPL002>
from pprint import pprint
toto = 1
titi = 2
pprint(titi + toto)  # ignored error
...
```

#### library errors

```python
# <printlinter disable-file PPL000>
import sys
toto = 1
titi = 2
print(titi + toto)  # ignored error
sys.stdout.write(titi + toto)  # ignored error
...
```

#### All errors

```python
# <printlinter disable-file ALL>
from sys import stdout, stderr
from pprint import pprint
toto = 1
titi = 2
print(titi + toto)  # ignored error
pprint(titi + toto)  # ignored error
stdout.write(titi + toto)  # ignored error
stderr.write(titi + toto)  # ignored error
stdout.writelines(titi + toto)  # ignored error
stderr.writelines(titi + toto)  # ignored error
...
```

## Ignore a block of code

To ignore a block of code (disable the linter) on a rules or all rules (disable library
rules come later), add a comment before the block you want ignore:
`<printlinter disable (error_code)`. To re enable the linter add an other comment after
the block of code: `<printlinter enable (error_code)>`. You are don't have to re enable
the linter after disabled it.

<!-- markdownlint-disable-next-line MD024 -->
### Examples

<!-- markdownlint-disable-next-line MD024 -->
#### Simple error

```python
from pprint import pprint
# <printlinter disable PPL001>
print("toto") # ignored error
pprint("titit")
# <printlinter enable PPL001>
...
```

You can nested ignored block.

```python
from pprint import pprint

# <printlinter disable PPL002>

pprint("titi") # ignored error

# <printlinter disable PPL001>
print("toto") # ignored error
# <printlinter enable PPL001>

print("tutu") # NOT IGNORED ERROR
pprint("tata") # ignored error

# <printlinter enable PPL002>
...
```

without re enable the linter.

```python
from pprint import pprint
# <printlinter disable PPL001>
print("toto") # ignored error
pprint("titit")
...
print('toto') # ignored error
```

<!-- markdownlint-disable-next-line MD024 -->
#### All errors

```python
from sys import stdout, stderr
from pprint import pprint
toto = 1
titi = 2
# <printlinter disable ALL>
print(titi + toto)  # ignored error
pprint(titi + toto)  # ignored error
stdout.write(titi + toto)  # ignored error
stderr.write(titi + toto)  # ignored error
stdout.writelines(titi + toto)  # ignored error
stderr.writelines(titi + toto)  # ignored error
# <printlinter enable ALL>
...
```

# Configuration

You can configurate the linter with a configuration file (configuration by command line,
will arrive in a future version).

PrintLinter supports 3 differents file type.

- `.yaml/.yml`
- `.json`
- `.toml`

By default the linter use one of thoses files load in this order.

- `printlinter.yaml`
- `printlinter.yml`
- `printlinter.json`
- `printlinter.toml`
- `pyproject.toml`

Alternatively, you can use another file and fill it in by running linter from the command
line.

```sh
printlinter lint <file|folder> --config-file </path/of/config/file>
```

## Target version

The config file allows to specify the python target version for the parser. Use a
string like this `3.10` or `3.7` to specify the version.

<!-- markdownlint-disable-next-line MD036 -->
**The python target version MUST be contains between 3.7 and 3.12**

You can see examples of this config [here](#examples-of-configuration-files).

## Ignored files

The config file allows to ignore files, unlike the comment that allows errors to be
ignored in a whole file this configuration option prevents the linter from reading the file.

You can see examples of this config [here](#examples-of-configuration-files).

## Disabled rules

The config file allows to disable rules, in all files and folders.

You can see examples of this config [here](#examples-of-configuration-files).

## Color

The config file allows to enable or disable colorized output. By default the `color` option
is on `True`.

You can see examples of this config [here](#examples-of-configuration-files).

## Examples of configuration files

### Yaml/Yml configuration file

```yaml
printlinter:
  target_version: "3.10"
  ignored_files: [toto.py]
  disabled_rules: [PPL001]
  color: true
```

### Json configuration file

```json
{
  "printlinter": {
    "target_version": "3.10",
    "ignored_files": ["toto.py"],
    "disabled_rules": ["PPL001"],
    "color": false
  }
}

```

### Toml configuration file

```toml
[printlinter]
target_version = "3.10"
ignored_files = ["toto.py"]
disabled_rules = ["PPL001"]
color = true
```

### Pyproject configuration file

```toml
[tool.printlinter]
target_version = "3.10"
ignored_files = ["toto.py"]
disabled_rules = ["PPL001"]
color = false
```

# But then

Too see the next features to be developed see [TODO](TODO.md). Here's a small,
non-exhaustive list of what's comming in the future versions.

- Lint display functions from other libraries.
