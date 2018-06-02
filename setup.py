#!/usr/bin/env python3
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name = 'MusixLI',
    version = '1.0',
    description = 'A command line application that lets you search for different artists, albums, songs and their lyrics.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Yathartha Goel',
    license = 'MIT License',
    platforms = 'Cross Platform',
    packages = setuptools.find_packages(),
    py_modules = ['musixli_main'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        'Click',
        'pymusixmatch',
        'prompt_toolkit',
        'pygments'
    ],
    entry_points = '''
        [console_scripts]
        musixli = musixli_main.main:cli
        msx = musixli_main.main_msx:cli
    ''',
    )
