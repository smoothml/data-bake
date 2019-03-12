# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Requirements
* [GNU Make](https://www.gnu.org/software/make/)
* {{ cookiecutter.python_interpreter|capitalize }}

## Usage
### `make` commands

| Command                   | Description |
| ------------------------- | ----------- |
| `make create_environment` | Create a [Python virtual environment](https://docs.python-guide.org/dev/virtualenvs/). |
| `make sync_data_to_s3`    | Sync data and models to [Amazon S3](https://aws.amazon.com/s3/) bucket {{ cookiecutter.s3_bucket }}. |
| `make sync_data_from_s3`  | Sync data and models from [Amazon S3](https://aws.amazon.com/s3/) bucket {{ cookiecutter.s3_bucket }}. |

Note, syncing to S3 for the first time will create the bucket {{ cookiecutter.s3_bucket }} if it does not already exist.

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
├ notebooks             <- Jupyter notebooks. Naming convention is a of the form
│                          <step>.<version>-<initials>-<description>.ipynb
│                          For example 01.0-PH-really-interesting-analysis.ipynb.
├ outputs               <- Generated outputs, such as figures or reports.
├ resources             <- Useful resources (e.g. relevant papers).
├ requirements.txt      <- Python requirements file for reproducing the analysis environment.
├ setup.py              <- Allows pip installation of src as a package.
└ src                   <- Source code for use in the project.
    └ __init__.py
```

<p><small>Project based on the <a href="https://cookiecutter.readthedocs.io">Cookiecutter</a> <a href="https://github.com/smoothml/cookiecutter-simple-data-science">simple data science</a> project template.</p>
\
