import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "downlink",
    version = "0.0.7",
    author = "Jake Kara",
    author_email = "jake@jakekara.com",
    description = ("Download all the documents linked from a web page."),
    license = "GPL-3",
    keywords = "example documentation tutorial",
    # repository_url = "https://github.com/jakekara/downlink-py",
    url = "https://github.com/jakekara/downlink-py",    
    packages=['downlink', 'tests'],
    long_description=read('README'),
    entry_points={
        'console_scripts': [
            'downlink = downlink.__main__:main',
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",        
    ],
    install_requires=[
        "bs4",
        "future"
    ]
)
