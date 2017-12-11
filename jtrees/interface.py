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


def construct_example_simpletree_structure(selectable_nodes=True, children=3):

    Text = FocusableText if selectable_nodes else urwid.Text

    json_data = requests.get('https://fakeuser-92f5d.firebaseio.com/thing.json')
    json_data.raise_for_status()

    json_data = json_data.json()

    # define root node
    tree = [Text('ROOT'), []]
    cli.traverse_dict(json_data, tree)

    # # define some children
    # c = g = gg = 0  # counter
    # for i in range(children):
    #     subtree = (Text('Child {0:d}'.format(c)), [])
    #     # and grandchildren..
    #     for j in range(children):
    #         subsubtree = (Text('Grandchild {0:d}'.format(g)), [])
    #         for k in range(children):
    #             leaf = (Text('Grand Grandchild {0:d}'.format(gg)), None)
    #             subsubtree[1].append(leaf)
    #             gg += 1  # inc grand-grandchild counter
    #         subtree[1].append(subsubtree)
    #         g += 1  # inc grandchild counter
    #     tree[1].append(subtree)
    #     c += 1
    return tree


def construct_example_tree(selectable_nodes=True, children=2):
    # define a list of tree structures to be passed on to SimpleTree
    forrest = [construct_example_simpletree_structure(selectable_nodes,
                                                      children)]

    # stick out test tree into a SimpleTree and return
    return SimpleTree(forrest)

def unhandled_input(k):
    #exit on q
    if k in ['q', 'Q']: raise urwid.ExitMainLoop()

def run():
    # get example tree
    stree = construct_example_tree()
    # Here, we add some decoration by wrapping the tree using ArrowTree.
    atree = ArrowTree(stree,
                      # customize at will..
                      # arrow_hbar_char=u'\u2550',
                      # arrow_vbar_char=u'\u2551',
                      # arrow_tip_char=u'\u25B7',
                      # arrow_connector_tchar=u'\u2560',
                      # arrow_connector_lchar=u'\u255A',
                      )

    # put the into a treebox
    treebox = TreeBox(atree)
    rootwidget = urwid.AttrMap(treebox, 'body')
    #add a text footer
    footer = urwid.AttrMap(urwid.Text('Q to quit'), 'focus')
    #enclose in a frame
    urwid.MainLoop(urwid.Frame(rootwidget, footer=footer), palette, unhandled_input = unhandled_input).run()  # go
