import setuptools
import requests
import os
from setuptools import setup
from zipfile import ZipFile

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ActflowToolbox",
    version="0.2.5.2",
    author="Cole MW, Ito T, Bassett DS, Schultz DH",
    author_email="michael.cole@rutgers.edu",
    description="Tools to quantify the relationship between connectivity \
    and task activity through network simulations and machine learning prediction. \
    Helps determine how connections contribute to specific brain functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ColeLab/ActflowToolbox",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free For Educational Use", # change according to chosen license type
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.0',
    install_requires=[
	   'numpy',
	   'scipy',
	   'nibabel',
	   'h5py',
	   'matplotlib',
	   'seaborn',
	   'statsmodels',
	   'functions',
       'zipfile37',
       'scikit-learn',
       'wbplot'
    ]
)