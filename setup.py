#!/usr/bin/env python3
from setuptools import setup
setup(
    name = 'MusixLI',
    version = '1.0',
    py_modules = ['musixli_main'],
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
