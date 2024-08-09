<!-- markdownlint-disable-file MD041 -->

Todo list of the project.

## Summary

- [Summary](#summary)
- [Next version](#next-version)
  - [Configuration](#configuration)
    - [Minimized output](#minimized-output)
    - [Pretty mode](#pretty-mode)
    - [Sortable output](#sortable-output)
    - [Add regex management for ignored\_files](#add-regex-management-for-ignored_files)
    - [Configuration options in command line](#configuration-options-in-command-line)
- [For the future](#for-the-future)
  - [Other libraries](#other-libraries)
  - [Configuration](#configuration-1)
    - [Add configuration option](#add-configuration-option)
    - [Add pre-commi hook](#add-pre-commi-hook)
  - [Documentation](#documentation)

## Next version

[Version 0.4.0](https://github.com/lilisse/printlinter/milestone/3)

<!-- markdownlint-disable-next-line MD024 -->
### Configuration

#### Minimized output

[Issue](https://github.com/lilisse/printlinter/issues/40)

Add minimized output with 3 level:

- 1, just the number of errors.
- 2, Number of errors and all files which contains errors (with the number by file).
- 3, Number of errors, files which contain errors, lines and error codes.

By default this option isn't activated.

#### Pretty mode

[Issue](https://github.com/lilisse/printlinter/issues/39)

Add a pretty mode for the output.

By default this option isn't activated.

#### Sortable output

[Issue](https://github.com/lilisse/printlinter/issues/35)

Add configuration to sort the output by files or by errors.

By default the output is sorted by files.

#### Add regex management for ignored_files

[Issue](https://github.com/lilisse/printlinter/issues/10)

Manage regex in ignored_files configuration option.

Examples: ignored_files: [toto/toto.py, toto/*, toto/*.py]

#### Configuration options in command line

[Issue](https://github.com/lilisse/printlinter/issues/11)

Add all configu options usable in command line.

## For the future

### Other libraries

- [ ] rich (100-199) [Issue](https://github.com/lilisse/printlinter/issues/8)

<!-- markdownlint-disable-next-line MD024 -->
### Configuration

#### Add configuration option

- [ ] ignored_file_with_regex [Issue](https://github.com/lilisse/printlinter/issues/10)

#### Add pre-commi hook

[Issue](https://github.com/lilisse/printlinter/issues/33)

### Documentation

- [ ] github pages
- [ ] readthedoc
