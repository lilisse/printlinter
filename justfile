# Remove python cache files
clean:
    find . \( -name __pycache__ -o -name "*.pyc" \) -delete

# Clear and display pwd
clear:
    clear
    pwd

# Install no-dev dependencies with poetry
install: clean clear
    poetry install --no-dev --remove-untracked

# install all dependencies with poetry and npm
install-all: clean clear
    poetry install --remove-untracked
    npm install
    sudo npm install markdownlint-cli2 --global

# Launch exodam pytest
test: clean clear
    python3.10 -m pytest

# Launch test and clean
pytest: test clean

# Do a clean install of pre-commit dependencies
preinstall: clean clear
    pre-commit clean
    pre-commit autoupdate
    pre-commit install --hook-type pre-merge-commit
    pre-commit install --hook-type pre-push
    pre-commit install --hook-type post-rewrite
    pre-commit install-hooks
    pre-commit install

# Simulate a pre-commit check on added files
prepre: clean clear
    #!/usr/bin/env sh
    set -eux pipefail
    git status
    pre-commit run --all-files

# Launch docstring verification with pydocstyle
pydocstyle path="py_linq_sql": clean clear
    pydocstyle {{ path }}

# Launch the mypy type linter on the module
mypy: clean clear
    mypy --pretty -p py_linq_sql --config-file pyproject.toml

# Run pylint
pylint path="py_linq_sql": clean clear
    pylint --output-format=colorized --msg-template='{msg_id}: in the file: {path}, at line: {line:}, at column: {column}, in objects: {obj} -> {msg}' {{ path }}

# Run flakehell
flakehell path="py_linq_sql": clean clear
    flakehell lint {{ path }}

# Run markdownlint
lintmd path='"**/*.md" "#node_modules"': clean clear
    markdownlint-cli2-config ".markdownlint-cli2.yaml" {{ path }}

# Run all linter
lint : clean clear pydocstyle mypy pylint flakehell lintmd

# Run black and isort
onmy31 path ="py_linq_sql tests": clean clear
    black {{path}}
    isort {{path}}

# auto interactive rebase
autorebase: clean clear
    git rebase -i $(git merge-base $(git branch --show-current) main)

# rebase on main
rebaseM: clean clear
    git checkout main
    git pull
    git checkout -
    git rebase main

# List of all just commands
list:
    just --list
