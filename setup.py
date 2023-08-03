"""
Run `conda env create --file environment.yaml` to create an editable 
install of this project
"""

from setuptools import setup, find_packages

PACKAGE_NAME = "project1"
setup(
    name=PACKAGE_NAME,
    version="0.1.0",
     # Specify the package directory
    package_dir={'': 'src'},
    # Include all files from the src directory
    package_data={PACKAGE_NAME: ['*']}
)
