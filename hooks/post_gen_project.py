import os


LICENSE = "{{ cookiecutter.license }}"

if LICENSE == "None":
    os.remove("LICENSE")
