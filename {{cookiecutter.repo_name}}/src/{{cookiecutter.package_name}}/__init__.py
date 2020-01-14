from {{ cookiecutter.package_name }}.config import PACKAGE_ROOT


with open('VERSION', 'r') as version_file:
    __version__ = version_file.read().strip()
