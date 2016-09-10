# -*- coding: utf-8 -*-

import os
import click
import jsonformat


@click.command()
@click.argument('json_file', type=click.File('r'))
def cli(json_file):
    try:
        print(jsonformat.jsonformat(json_file))
    except ValueError:
        path = os.path.realpath(json_file.name)
        msg = '{path} is not a valid JSON'.format(path=path)
        raise click.ClickException(msg)
