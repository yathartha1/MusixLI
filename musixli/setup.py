from setuptools import setup
setup(
    name = 'MusixLI',
    version = '1.0',
    py_modules = ['musixli'],
    install_requires = [
        'Click',
        'pymusixmatch',
    ],
    entry_points = '''
        [console_scripts]
        musixli = musixli:start
    ''',
    )
