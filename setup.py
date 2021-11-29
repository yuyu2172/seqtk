#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="seqtk",
    version="0.5.0",
    description="seqtk provides various tools for Sequence.",
    author="Yusuke Niitani",
    author_email="",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    package_data={"seqtk": ["py.typed"]},
    url="https://github.com/yuyu2172/seqtk",
)
