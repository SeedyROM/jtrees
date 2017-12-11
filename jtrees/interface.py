#!/usr/bin/python
# Copyright (C) 2013  Patrick Totzke <patricktotzke@gmail.com>
# This file is released under the GNU GPL, version 3 or a later revision.

from urwidtrees.decoration import CollapsibleArrowTree  # for Decoration
from urwidtrees.tree import SimpleTree
from urwidtrees.nested import NestedTree
from urwidtrees.widgets import TreeBox
import urwid
import requests

from .widgets.generic import FocusableText

palette = [
    ('body', 'light green', 'black'),
    ('focus', 'light magenta', 'dark gray', 'standout'),
    ('bars', 'dark green', 'white', ''),
    ('arrowtip', 'light blue', 'light gray', ''),
    ('connectors', 'light red', 'light gray', ''),
]

def generate_urwid_tree_from_dict(d, tree):
    '''Traverse a dictionary recursively and creates a valid Urwid tree.

    Args:
        d (dict or iterable): Dictionary to traverse.
        tree (list): State to alter with side effects.

    Returns: None
    '''
    if isinstance(d, list):
        for _d in d:
            generate_urwid_tree_from_dict(_d, tree)
    else:
        for k, v in d.items():
            if isinstance(v, dict):
                subtree = [urwid.SelectableIcon(str(f'{k}')), list()]
                generate_urwid_tree_from_dict(v, subtree)
            else:
                subtree = [urwid.Text(str(f'{k}: {v}')), None]

            tree[1].append(subtree)

def http_get_json(url):
    ''' get json from any web source '''

    json_data = requests.get(url)
    json_data.raise_for_status()

    json_data = json_data.json()

    return json_data

class JTreesCLI():
    @property
    def forrest(self):
        json_url = 'https://fakeuser-92f5d.firebaseio.com/thing.json'
        json_data = http_get_json(json_url)

        tree = [FocusableText('ROOT'), []]
        generate_urwid_tree_from_dict(json_data, tree)

        # Must return a list of nodes.
        return [tree]

    def unhandled_input(self, key):
        ''' call back from MainLoop '''
        if key in ['q', 'Q']:
            raise KeyboardInterrupt
        if key == ' ':
            x = self.tree_box.get_focus()
            import pudb; pudb.set_trace()

    def __init__(self):
        self.tree = SimpleTree(self.forrest)
        self.tree_box = TreeBox(CollapsibleArrowTree(self.tree))

        self.widget = urwid.AttrMap(self.tree_box, 'body')
        self.footer = urwid.AttrMap(urwid.Text('Q to quit'), 'focus')

    def run(self):
        try:
            urwid.MainLoop(urwid.Frame(self.widget, footer=self.footer),
                           palette, unhandled_input=self.unhandled_input).run()
        except KeyboardInterrupt:
            print('☮  Peace! ☮')
            return
