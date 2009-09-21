#!/usr/bin/env python
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 4):
    sys.exit("requires python 2.4 and up")


setup(name="rpyc",
    version = "__MAJOR__.__MINOR__.__REVISION__",
    description = "Remote Python Call (RPyC), a transparent and symmetric RPC library",
    author = "Tomer Filiba",
    author_email = "tomerfiliba@gmail.com",
    license = "MIT",
    url = "http://rpyc.wikidot.com",
    packages = ['rpyc', 'rpyc.core', 'rpyc.utils', 'rpyc.servers'],
    long_description = ("A symmetric library for transparent RPC, clustering and "
    "distributed computing for python, built around the concept of remote "
    "services and object proxying"),
    platforms = ["POSIX","Windows"],
)

