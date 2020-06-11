# Module: autosentiment
# Author: Sazin Reshed Samin <sazinsamin50@gmail.com>
# License: MIT

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autosentiment", # Replace with your own username
    version="1.1.4",
    author="Sazin Reshed Samin",
    author_email="sazinsamin50@gmail.com",
    description="An automatic sentiment analysis pakage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeFighter03/autosentiment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)