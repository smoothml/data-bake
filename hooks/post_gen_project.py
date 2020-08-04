import os


license = "{{ cookiecutter.license }}"
package_manager = "{{ cookiecutter.package_manager }}"

if license == "None":
    os.remove("LICENSE")

if package_manager == "pip":
    os.remove("environment.yaml")
elif package_manager == "conda":
    os.remove("requirements.txt")
else:
    raise ValueError("Unrecognised package manager.")
