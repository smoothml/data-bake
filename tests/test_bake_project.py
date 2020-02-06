import os
from contextlib import contextmanager
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()

    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)

    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project.basename == 'project-name'

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'data' in found_toplevel_files
        assert 'models' in found_toplevel_files
        assert 'notebooks' in found_toplevel_files
        assert 'outputs' in found_toplevel_files
        assert 'src' in found_toplevel_files
        assert '.env' in found_toplevel_files
        assert '.gitignore' in found_toplevel_files
        assert 'Makefile' in found_toplevel_files
        assert 'pytest.ini' in found_toplevel_files
        assert 'README.md' in found_toplevel_files
        assert 'requirements.txt' in found_toplevel_files
        assert 'setup.cfg' in found_toplevel_files
        assert 'LICENSE' not in found_toplevel_files


def test_bake_with_license(cookies):
    with bake_in_temp_dir(cookies, extra_context={'license': 'MIT'}) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'LICENSE' in found_toplevel_files
