import io
import os

from setuptools import setup, find_packages


def getRequires():
    deps = ["requests"]
    return deps


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, "README.md"), encoding="utf-8").read()


setup(
    name="sepulsa",
    version="0.1",
    author="Kelvin Desman",
    author_email="kelvindsmn@gmail.com",
    url="https://github.com/vousmeevoyez/sepulsa",
    packages=find_packages(exclude=["temp*.py", "test"]),
    include_package_data=True,
    description="Unofficial Sepulsa library for Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=getRequires(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
