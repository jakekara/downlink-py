import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dl_docs",
    version = "0.0.0",
    author = "Jake Kara",
    author_email = "jake@jakekara.com",
    description = ("Download all the documents linked from a web page."),
    license = "GPL-3",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/dl_docs",
    packages=['dl_docs', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3",
    ],
)
