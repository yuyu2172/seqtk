#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="seqtk",
    version="0.0.1",
    description="",
    author="Yusuke Niitani",
    author_email="",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    package_data={"seqtk": ["py.typed"]},
)
