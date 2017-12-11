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

from . import interface


def traverse_dict(d, tree):
    '''Traverse a dictionary recursively and call an arbitrary function.

    Args:
        d (dict or iterable): Dictionary to traverse.
        f (callable): Function to call every end of branch.

    Returns: None
    '''
    if isinstance(d, list):
        for _d in d:
            traverse_dict(_d, tree)
    else:
        for k, v in d.items():
            if isinstance(v, dict):
                subtree = [urwid.SelectableIcon(str(f'{k}')), list()]
                traverse_dict(v, subtree)
            else:
                subtree = [urwid.Text(str(f'{k}: {v}')), None]

            tree[1].append(subtree)


def start_urwid():
    '''Start urwid, and handle KeyboardInterrupt.

    Args: None
    Returns: None
    '''
    tree_widget = urwidtrees.widgets.TreeBox(
        urwidtrees.decoration.CollapsibleIndentedTree(
            urwidtrees.tree.SimpleTree([
                (urwid.SelectableIcon(kwargs['FILE']), (
                    (urwid.SelectableIcon('sub item 1'), None),
                    (urwid.SelectableIcon('sub item 2'), None),
                )),
                (urwid.SelectableIcon('item 2'), None),
            ])
        )
    )

    try:
        # See if we got a SIGINT!
        urwid.MainLoop(tree_widget).run()
    except KeyboardInterrupt:
        # Peace out.
        print('☮  Peace! ☮')
        return


def main(*args, **kwargs):
    '''The main entry point.

    Args:
        kwargs (dict): from docopt

    Return: None
    '''
    # json_data = requests.get('https://jsonplaceholder.typicode.com/posts')
    # json_data.raise_for_status()
    #
    # json_data = json_data.json()



    # traverse_dict(json_data, f=lambda x: x)
    interface.run()


if __name__ == '__main__':
    kwargs = docopt(__doc__)
    main(**kwargs)
