# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Requirements
* [GNU Make](https://www.gnu.org/software/make/)
* Python 3.5 or above

## Usage
### `make` commands

| Command                   | Description |
| ------------------------- | ----------- |
| `make create_environment` | Create a [Python virtual environment](https://docs.python-guide.org/dev/virtualenvs/). |

## Project Structure
```
{{ cookiecutter.repo_name }}
├ Makefile              <- Makefile with helpful make commands.
├ README.md             <- Top-level README for project developers.
├ .env                  <- Secrets. DO NOT SOURCE CONTROL!
├ data
│   ├ external          <- Data from external sources.
│   ├ interim           <- Intermediate, transformed data.
│   ├ processed         <- Final, canonical data sets from modelling.
│   ├ raw               <- Original, immutable raw data sets.
│   └ results           <- Results of modelling and analysis.
├ models                <- Trained and serialized models, model predictions, or model summaries.
├ notebooks             <- Jupyter notebooks.
├ outputs               <- Generated outputs, such as figures or reports.
├ resources             <- Useful resources (e.g. relevant papers).
├ requirements.txt      <- Python requirements file for reproducing the analysis environment.
└ src                   <- Source code for use in the project comprising a Python package and tests.
    ├ {{ cookiecutter.package_name }}
    │   ├ __init__.py
    │   ├ config.py
    │   └ VERSION
    ├ tests
    │   └ __init__.py
    └ setup.py
```
Project based on the [Cookiecutter](https://cookiecutter.readthedocs.io) [simple data science](https://github.com/smoothml/cookiecutter-simple-data-science) project template.
