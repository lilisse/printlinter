# Standard imports
from contextlib import contextmanager
from os import chdir, getcwd
from pathlib import Path
from typing import Generator


@contextmanager
def change_cwd(new_cwd: Path) -> Generator[None, None, None]:
    old_cwd = getcwd()
    chdir(new_cwd)
    yield
    chdir(old_cwd)
