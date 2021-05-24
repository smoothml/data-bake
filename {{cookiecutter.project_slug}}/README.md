# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

## Requirements
- [GNU Make](https://www.gnu.org/software/make/)
- Python {{ cookiecutter.python_version }}
- [Poetry](https://python-poetry.org/)

## Usage
Most actions are performed via the `Makefile`. In particular:
- Create your Poetry environment with `make install`.
- Run tests with `make test`.
- Run [Flake8](https://flake8.pycqa.org/en/latest/) linting checks with `make quality`.
- Format your code using [Black](https://black.readthedocs.io/en/stable/) and [Isort](https://black.readthedocs.io/en/stable/) with `make format`.

## Project structure
```shell
{{ cookiecutter.project_slug }}
├── Makefile                          # Useful commands. Run make to see a list.
├── pyproject.toml                    # Project configuration.
├── README.md                         # Project information.
├── setup.cfg                         # Project configuration (Flake8).
├── data                              # Project data.
├── models                            # Trained models.
├── notebooks                         # Notebooks for prototyping and research.
├── {{ cookiecutter.package_name }}   # Application package.
│ └── __init__.py
└── tests                             # Application tests.
    └── __init__.py
```
Project based on the [DataBake](https://github.com/smoothml/data-bake) template.
