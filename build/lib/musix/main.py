#!/usr/bin/env python3
from .musixli import musixli

def cli():
    m = musixli()
    m.start()

if __name__ == "__main__":
    cli()
