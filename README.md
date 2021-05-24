# Data Bake
![Tests](https://github.com/smoothml/data-bake/actions/workflows/test.yml/badge.svg)

DataBake is a simple data science project template based on the [Cookiecutter](https://cookiecutter.readthedocs.io) templating engine and heavily inspired by the excellent [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science).

## Assumptions
This project template makes certain assumptions. These are:
* Your data science project uses Python.
* You're working in a *nix environment. Cookiecutter will give you project structure in Windows, but some features of this template may not work.

## Requirements
* Python >= 3.8.
* [Cookiecutter](https://cookiecutter.readthedocs.io) >= 1.7.0
* [GNU Make](https://www.gnu.org/software/make/)

## Usage
To start a new project, run:
```
cookiecutter https://github.com/smoothml/data-bake
```
You will be asked to provide the variables described below.

| Variable | Description |
| -------- | ----------- |
| `project_name` | Name of your project. |
| `project_slug` | Root folder for you repository. Defaults to lower case `project_name` with spaces and underscores replaced with hyphens. |
| `package_name` | Name of your source code package. Defaults to `project_slug` with underscores instead of hyphens. |
| `author_name` | Your name, or name of your project or organization. |
| `author_email` | Contact email address. |
| `description` | A short description of your project. |
| `python_version` | Python version, either defaults to 3.9. |

The resulting project structure is:
```shell
project_slug
├── Makefile          # Useful commands. Run make to see a list.
├── pyproject.toml    # Project configuration.
├── README.md         # Project information.
├── setup.cfg         # Project configuration (Flake8).
├── data              # Project data.
├── models            # Trained models.
├── notebooks         # Notebooks for prototyping and research.
├── package_name      # Application package.
│ └── __init__.py
└── tests             # Application tests.
    └── __init__.py
```
