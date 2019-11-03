# Simple Data Science Cookiecutter
A template data science project structure. This is a simplified version of the excellent [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science).

## Assumptions
This project template makes certain assumptions. These are:
* Your data science project uses Python.
* You're working in a *nix environment. Cookiecutter will give you project structure in Windows, but some features of this template may not work.
* You're using AWS for data storage. Support for other cloud providers will be added at a later date.

## Requirements
* Python >= 3.5.
* [Cookiecutter](https://cookiecutter.readthedocs.io) >= 1.6.0

## Usage
To start a new project, run:
```
cookiecutter https://github.com/smoothml/cookiecutter-simple-data-science
```
You will be asked to provide the variables described below.

| Variable | Description |
| -------- | ----------- |
| `project_name` | Name of your project. |
| `repo_name` | Name of your repository. Defaults to lower case `project_name` with spaces and underscores replaced with hyphens. |
| `package_name` | Name of your source code package. Defaults to `repo_name` with underscores instead of hyphens. |
| `author_name` | Your name, or name of your project or organization. |
| `description` | A short description of your project. |
| `s3_bucket` | Name of Amazon S3 bucket for storing your data and models. If you're not using S3 leave this as the default value and never speak of it again! |
| `aws_profile` | Name of AWS profile for accessing the S3 bucket. Again, if you're not using S3 ignore this. |
| `license` | A choice of several open source licenses. Choose "None" if your project is not open source. |

The resulting project structure is:
```
├ Makefile              <- Makefile with helpful make commands.
├ README.md             <- Top-level README for project developers.
├ LICENSE               <- License file (unless no license was specified).
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
