from pathlib import Path
from setuptools import find_packages, setup

NAME = '{{ cookiecutter.repo_name }}'
DESCRIPTION = '{{ cookiecutter.description }}'
REQUIRES_PYTHON = '>=3.5.0'
AUTHOR = '{{ cookiecutter.author_name }}'

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / '{{ cookiecutter.package_name }}'

# Get package version
with open(PACKAGE_DIR / 'VERSION') as f:
    VERSION = f.read().strip()

REQUIREMENTS = []

setup(
    name=NAME,
    packages=find_packages(exclude=['tests']),
    version=VERSION,
    description=DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIREMENTS,
    author=AUTHOR
)
