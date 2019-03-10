import sys
import os


license = "{{ cookiecutter.license }}"

if license == "None":
    os.remove("LICENSE")
