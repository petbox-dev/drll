"""
Drilling Calculations Library

Author
------
Connor Elliott

Notes
-----
Created on October 5, 2020
"""

import setuptools, os, sys, re

from petbox.drll import __version__

try:
    from setuptools import setup  # type: ignore
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drll",
    version="0.0.1",
    author="Connor Elliott",
    author_email="connor@con-struct.solutions",
    description="Driling Calculations Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petbox-dev/drll",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    license='MIT',
    install_requires=['numpy', 'scipy'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - PRE-ALPHA',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Typing :: Typed'
    ],
    keywords=[
        'petbox-drll', 'drll', 'drilling', 'drill','petroleum drilling'
    ],
)

