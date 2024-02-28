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

# Launch the mypy type linter on the module
mypy-linter: clean clear
    mypy --pretty -p py_printlinter --config-file pyproject.toml

# Launch the mypy type linter on the module
mypy-cli: clean clear
    mypy --pretty -p cli_app --config-file pyproject.toml


# Run markdownlint
lintmd path='"**/*.md" "#node_modules"': clean clear
    markdownlint-cli2-config ".markdownlint-cli2.yaml" {{ path }}

# Run ruff
ruff path="py_printlinter cli_app": clean clear
    ruff {{path}}

# Run black and isort
onmy31 path ="py_printlinter cli_app tests": clean clear
    black {{path}}
    isort {{path}}

# Run all linter
lint : clean clear onmy31 mypy-linter mypy-cli ruff lintmd

# auto interactive rebase
autorebase: clean clear
    git rebase -i $(git merge-base $(git branch --show-current) main)

# Launch coverage on all
coverage: clean clear
    coverage run -m pytest
    clear
    coverage report -m --skip-covered --precision=3


# rebase on main
rebaseM: clean clear
    git checkout main
    git pull
    git checkout -
    git rebase main

# List of all just commands
list:
    just --list
