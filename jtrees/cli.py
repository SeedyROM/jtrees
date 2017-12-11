'''
Usage: jtrees FILE [-v]

Options:
    -v --version                        Displays the version.
'''
import urwid
import urwidtrees
import requests
import json

from docopt import docopt

from . interface import JTreesCLI


def main(*args, **kwargs):
    '''The main entry point.

    Args:
        kwargs (dict): from docopt

    Return: None
    '''
    jtrees = JTreesCLI()
    jtrees.run()


if __name__ == '__main__':
    kwargs = docopt(__doc__)
    main(**kwargs)
