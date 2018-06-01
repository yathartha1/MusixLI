#!/usr/bin/env python3
from .msx_cli import msx_cli

def cli():
    msx = msx_cli()
    msx.begin()

if __name__ == "__main__":
    cli()
