#!/usr/bin/python

try:
    # this is primarily to support the 'develop' target
    # if setuptools/distribute are installed
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pylibftdi",
    version="0.14",
    description="Pythonic interface to FTDI devices using libftdi",
    long_description=open('README.rst').read(),
    author="Ben Bass",
    author_email="benbass@codedstructure.net",
    url="http://bitbucket.org/codedstructure/pylibftdi",
    packages=["pylibftdi", "pylibftdi.examples"],
    scripts=["scripts/ftdi_osx_driver_reload",
             "scripts/ftdi_osx_driver_unload"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Hardware"
    ]
)
