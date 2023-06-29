from setuptools import setup
from setuptools.command.install import install
import sys
import subprocess
from subprocess import getoutput

setup(
    name="latincy_ext",
    version="0.0.1",
    packages=["latincy_ext"],
    url="https://github.com/diyclassics/latincy_ext",
    license="MIT License",
    readme="README.md",
    author="Patrick J. Burns",
    author_email="patrick@diyclassics.org",
    description="Custom components for use with the LatinCy models",
    install_requires=[
        "spacy~=3.5.3",
        "spacy-transformers~=1.2.3",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
