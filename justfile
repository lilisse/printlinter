# Remove python cache files
clean:
    -find . \( -name __pycache__ -o -name "*.pyc" \) -delete

# Clear and display pwd
clear:
    clear
    pwd

# Install no-dev dependencies with poetry
install: clean clear
    poetry install --no-dev --sync

# install all dependencies with poetry and npm
install-dev: clean clear
    poetry install --sync

create_rep_for_test:
    ./create_ignored_rep_for_test.sh

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
    mypy --pretty -p printlinter --config-file pyproject.toml

# Launch the mypy type linter on the module
mypy-cli: clean clear
    mypy --pretty -p cli_app --config-file pyproject.toml


# Run ruff
ruff path="printlinter cli_app": clean clear
    ruff {{path}}

# Run black and isort
onmy31 path ="printlinter cli_app tests": clean clear
    black {{path}}
    isort {{path}}

# Run all linter
lint : clean clear onmy31 mypy-linter mypy-cli ruff

# auto interactive rebase
autorebase: clean clear
    git rebase -i $(git merge-base $(git branch --show-current) main)

# Launch coverage on all
coverage: clean clear
    pytest --cov-report term-missing:skip-covered --cov

# rebase on main
rebaseM: clean clear
    git checkout main
    git pull
    git checkout -
    git rebase main

# List of all just commands
list:
    just --list
