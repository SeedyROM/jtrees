#!/usr/bin/python
# Copyright (C) 2013  Patrick Totzke <patricktotzke@gmail.com>
# This file is released under the GNU GPL, version 3 or a later revision.

from urwidtrees.decoration import ArrowTree  # for Decoration
from urwidtrees.tree import SimpleTree
from urwidtrees.widgets import TreeBox
import urwid
import requests

from . import cli

palette = [
    ('body', 'black', 'light gray'),
    ('focus', 'light gray', 'dark blue', 'standout'),
    ('bars', 'dark blue', 'light gray', ''),
    ('arrowtip', 'light blue', 'light gray', ''),
    ('connectors', 'light red', 'light gray', ''),
]

class FocusableText(urwid.WidgetWrap):
    """Selectable Text used for nodes in our example"""
    def __init__(self, txt):
        t = urwid.Text(txt)
        w = urwid.AttrMap(t, 'body', 'focus')
        urwid.WidgetWrap.__init__(self, w)

    def selectable(self):
        return True

    def keypress(self, size, key):
        return key


def http_get_json(url):
    ''' get json from any web source '''

    json_data = requests.get(url)
    json_data.raise_for_status()

    json_data = json_data.json()

    return json_data


def construct_example_simpletree_structure(selectable_nodes=True, children=3):

    Text = FocusableText if selectable_nodes else urwid.Text

    json_url = 'https://fakeuser-92f5d.firebaseio.com/thing.json'

    json_data = http_get_json(json_url)

    # define root node
    tree = [Text('ROOT'), []]
    cli.traverse_dict(json_data, tree)

    return tree


def unhandled_input(k):
    ''' call back from MainLoop '''
    # exit on q
    if k in ['q', 'Q']:
        raise urwid.ExitMainLoop()


def run():
    # get example tree
    forrest = [construct_example_simpletree_structure()]

    tree = SimpleTree(forrest)

    # Here, we add some decoration by wrapping the tree using ArrowTree.
    tree = ArrowTree(tree)

    # put the into a treebox
    treebox = TreeBox(tree)

    rootwidget = urwid.AttrMap(treebox, 'body')
    # add a text footer
    footer = urwid.AttrMap(urwid.Text('Q to quit'), 'focus')
    # enclose in a frame

    # start the curses interface
    urwid.MainLoop(urwid.Frame(rootwidget, footer=footer),
                   palette, unhandled_input=unhandled_input).run()
