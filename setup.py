# setup.py
# Setup installation for the application

from setuptools import find_namespace_packages, setup
import os

BASE_DIR = os.environ.get("BASE_DIR", None)
BASE_DIR = "." if BASE_DIR is None else BASE_DIR

# Load packages from requirements.txt
with open(f"{BASE_DIR}/requirements.txt") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

dev_packages = [
    "black==21.9b0",
    "flake8==3.9.2",
    "ipykernel==5.5.5",
    "ipython==7.16.1",
    "isort==5.9.3",
    "jedi==0.18.0",
    "jupyter-client==7.0.2",
    "jupyter-core==4.7.1",
    "mypy-extensions==0.4.3",
    "pyflakes==2.3.1",
    "pylint==2.10.2",
]

setup(
    name="mailsender",
    version="0.2.0",
    license="Apache",
    description="A simple mail sender.",
    author="Alberto Burgos Plaza",
    author_email="aburgos@cimne.upc.edu",
    url="https://github.com/aburgoscimne/mail-sender",
    python_requires=">=3.6",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "dev": dev_packages,
    },
)
