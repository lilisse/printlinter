<!-- markdownlint-disable-file MD024 -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add a configuration option to sort the output: `sorted_by`.
  Possible values:

  - files to sort by files name.
  - errors to sort by errors code.

- Add a configuration option for a minimize output: `output_level`.
  Possible values:

  - 1 for a really short output with just the number of errors
  - 2 for a short output with number of errors by files
  - 3 for a medium output with number of errors by files and which error and at which lines

## [0.3.0] - 09-08-2024

### Added

- Add bdd test with [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/).
- Add tests on real projects.

## [0.2.0] - 23-05-2024

### Added

- Now we can ignore a block of code and don't re enable the linter.
- Add a way to ignore a block of code with: `<printlinter disable PPLXXX>` to disable
  linter and: `<printlinter enable PPLXXX>` to re enable it. We can also disable
  `ALL` rules.
- Add a configuration option to enable/disable colorized output: `color`.
[Issue](https://github.com/lilisse/printlinter/issues/6).
- Add a way to ignore next line with: `<printlinter disable-next PPLXXX>`.
[Issue](https://github.com/lilisse/printlinter/issues/1).
- Add default `ignored_rep` configuration. All those folders while not be visited by the
  linter.
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
- Add progress bar to the cli.

## [0.1.0] - 21-03-2024

### Added

- Add configuration files management with 3 options:
  - `target_version`
  - `ignored_files`
  - `disabled_rules`
- Add management of comments to ignore a line or a whole file.
- Add linters and formatters
- Add tests
- Add the `lint` verb to the cli to lint a folder and detect display function on python
  code. See [README.md](README.md) to understand how to use the linter.
