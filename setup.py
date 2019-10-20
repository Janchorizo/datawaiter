# -*- coding: utf8 -*-

import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open('requirements.txt' ,'r') as f:
    requirements = f.read().strip().split('\n')

setuptools.setup(
    name="datawaiter",
    version="0.1.0",
    author="Alejandro Rodríguez Díaz",
    author_email="jancho@usal.es",
    description="A simple Flask based server for easy CSV data and stat serving.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        'Documentation': 'https://datawaiter.readthedocs.io/en/latest/index.html',
        'Source': 'https://github.com/Janchorizo/datawaiter',
        'Tracker': 'https://github.com/Janchorizo/datawaiter/issues',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements
)
