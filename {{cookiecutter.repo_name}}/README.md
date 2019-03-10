# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

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
├ requirements.txt      <- Python requirements file for reproducing the analysis environment.
├ setup.py              <- Allows pip installation of src as a package.
└ src                   <- Source code for use in the project.
    └ __init__.py
```

<p><small>Project based on the <a href="https://cookiecutter.readthedocs.io">Cookiecutter</a> <a href="https://github.com/smoothml/cookiecutter-simple-data-science">simple data science</a> project template.</p>
