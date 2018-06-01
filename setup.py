from setuptools import setup
setup(
    name = 'MusixLI',
    version = '1.0',
    py_modules = ['musixli'],
    install_requires = [
        'Click',
        'pymusixmatch',
        'prompt_toolkit',
    ],
    entry_points = '''
        [console_scripts]
        musixli = musixli.main:cli
        msx = musixli.main_msx:cli
    ''',
    )
