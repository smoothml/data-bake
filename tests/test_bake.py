from contextlib import contextmanager
from pathlib import Path
import toml

from cookiecutter.utils import rmtree


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporary directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)

    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "project-name"

        found_toplevel_files = [f.name for f in result.project_path.glob("*")]
        assert "data" in found_toplevel_files
        assert "models" in found_toplevel_files
        assert "notebooks" in found_toplevel_files
        assert ".gitignore" in found_toplevel_files
        assert "Makefile" in found_toplevel_files
        assert "pyproject.toml" in found_toplevel_files
        assert "README.md" in found_toplevel_files
        assert "setup.cfg" in found_toplevel_files


def test_bake_with_new_name(cookies):
    name = "Awesome Project"
    project_slug = "awesome-project"
    package_name = "awesome_project"
    with bake_in_temp_dir(
        cookies,
        extra_context={"project_name": name},
    ) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == project_slug
        assert package_name in [p.name for p in list(result.project_path.glob("*"))]
        assert (
            (result.project_path / "README.md").open("r").readlines()[0].strip()
            == f"# {name}"
        )

        pyproject = toml.loads(
            (result.project_path / "pyproject.toml").open("r").read()
        )
        assert pyproject["tool"]["poetry"]["name"] == project_slug
        assert package_name in pyproject["tool"]["isort"]["src_paths"]
        assert f"{package_name}/*" in pyproject["tool"]["coverage"]["run"]["include"]


def test_bake_with_author(cookies):
    author_name = "Paul Harrison"
    author_email = "paul@harrison.sh"
    with bake_in_temp_dir(
            cookies,
            extra_context={
                "author_name": author_name,
                "author_email": author_email,
            },
    ) as result:
        pyproject = toml.loads(
            (result.project_path / "pyproject.toml").open("r").read()
        )
        assert (
            f"{author_name} <{author_email}>"
            in pyproject["tool"]["poetry"]["authors"]
        )


def test_bake_with_description(cookies):
    description = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent scelerisque "
        "ante mollis turpis eleifend rutrum."
    )
    with bake_in_temp_dir(
            cookies,
            extra_context={"description": description},
    ) as result:
        assert (
                (result.project_path / "README.md").open("r").readlines()[1].strip()
                == description
        )


def test_bake_with_python_version(cookies):
    python_versions = ["3.8", "3.9"]
    for python_version in python_versions:
        with bake_in_temp_dir(
            cookies,
            extra_context={"python_version": python_version},
        ) as result:
            assert result.project_path.is_dir()
            assert result.exit_code == 0
            assert result.exception is None

            pyproject = toml.loads(
                (result.project_path / "pyproject.toml").open("r").read()
            )
            assert (
                pyproject["tool"]["poetry"]["dependencies"]["python"]
                == f"^{python_version}"
            )
            assert (
                f"py{python_version.replace('.', '')}"
                in pyproject["tool"]["black"]["target-version"]
            )
