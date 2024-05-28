# Pytest imports
import pytest
from pytest import param

# Standard imports
import tarfile
import urllib.request as url_req
from io import BytesIO
from pathlib import Path

# Third party imports
from assertpy import assert_that, soft_assertions
from typer.testing import CliRunner

# First party imports
from cli_app import APP

RUNNER = CliRunner()


def _get_project(url: str, dest_folder: Path) -> None:
    raw_file = url_req.urlopen(url).read()
    opened_file = tarfile.open(fileobj=BytesIO(raw_file))
    opened_file.extractall(dest_folder)
    opened_file.close()


@pytest.mark.parametrize(
    "name, url, nb_errors, a_contained_error, file_of_error, line_col_of_error",
    [
        param(
            "mypy-1.10.0",
            "https://github.com/python/mypy/archive/refs/tags/v1.10.0.tar.gz",
            297,
            """`print(f"Cherry-picked \ncommit {commit} from {typeshed_dir}")` print-detected""",
            "cherry-pick-typeshed.py",
            "66:4",
            id="mypy",
        ),
        # TODO: Reactivate this test when we can put filename with regex in ignored file
        # param(
        #     "django-5.0.6",
        #     "https://github.com/django/django/archive/refs/tags/5.0.6.tar.gz",
        #     82,
        #     """`print("\tResource %s for language %s" % (resource, lang))` print-detected""",
        #     "manage_translations.py",
        #     "196:12",
        #     id="django",
        # ),
        param(
            "exoplanet.eu-v2.15.1",
            "https://gitlab.obspm.fr/exoplanet/exoplanet.eu/-/archive/v2.15.1/exoplanet.eu-v2.15.1.tar.gz",
            52,
            """`print(f"{tot_tested}/{tot_col} files tested so far")` print-detected""",
            "test_static_files.py",
            "156:8",
            id="exoplanet.eu",
        ),
        param(
            "exoimport-v1.4.1",
            "https://gitlab.obspm.fr/exoplanet/exoimport/-/archive/v1.4.1/exoimport-v1.4.1.tar.gz",
            8,
            """`print(text2art("Filtration"))` print-detected""",
            "translate.py",
            "93:4",
            id="exoimport",
        ),
        param(
            "py-linq-sql-v1.11.0-pre-release",
            "https://gitlab.obspm.fr/exoplanet/py-linq-sql/-/archive/v1.11.0-pre-release/py-linq-sql-v1.11.0-pre-release.tar.gz",
            2,
            "`print(record)` print-detected",
            "test_all_sign_op.py",
            "186:4",
            id="py-linq-sql",
        ),
        param(
            "boto3-1.34.114",
            "https://github.com/boto/boto3/archive/refs/tags/1.34.114.tar.gz",
            0,
            "",
            "",
            "",
            id="boto 3",
        ),
        param(
            "botocore-1.34.114",
            "https://github.com/boto/botocore/archive/refs/tags/1.34.114.tar.gz",
            6,
            "`print(self.event_emitter.emit.call_args_list[0][1]['section'].name)`",
            "test_example.py",
            "114:8",
            id="boto core",
        ),
        param(
            "urllib3-2.2.1",
            "https://github.com/urllib3/urllib3/releases/download/2.2.1/urllib3-2.2.1.tar.gz",
            3,
            """`print("Server teardown")` print-detected""",
            "conftest.py",
            "62:8",
            id="urllib 3",
        ),
        param(
            "requests-2.32.2",
            "https://github.com/psf/requests/releases/download/v2.32.2/requests-2.32.2.tar.gz",
            6,
            "`print(json.dumps(info(), sort_keys=True, indent=2))` print-detected",
            "help.py",
            "130:4",
            id="request",
        ),
    ],
)
@pytest.mark.slow()
def test_on_real_projects(
    tmp_path,
    pnv_soft_reset,
    name,
    url,
    nb_errors,
    a_contained_error,
    file_of_error,
    line_col_of_error,
):
    destination_folder = tmp_path / "TEST_REAL_PROJECTS"
    destination_folder.mkdir()
    _get_project(url, destination_folder)

    result = RUNNER.invoke(
        APP,
        [
            "lint",
            f"{destination_folder}/{name}",
            "--config-file",
            f"{Path(__file__).parent / 'config_real_projects.yml'}",
        ],
    )

    with soft_assertions():
        assert_that(result.exit_code).is_equal_to(0)
        assert_that(result.stdout).contains(
            f"Found {nb_errors} errors",
            a_contained_error,
            file_of_error,
            line_col_of_error,
        )