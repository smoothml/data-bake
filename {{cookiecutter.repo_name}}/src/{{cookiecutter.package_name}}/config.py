import {{ cookiecutter.package_name }}
from pathlib import Path


PACKAGE_ROOT = Path({{ cookiecutter.package_name }}.__file__).resolve().parent
