#!/usr/bin/env python3
import logging

from metamodel.generators.graphqlgen import cli

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    cli()
