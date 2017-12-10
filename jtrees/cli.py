import urwid
import urwidtrees
import requests
import json

json_data = requests.get('https://jsonplaceholder.typicode.com/posts')
json_data.raise_for_status()

json_data = json_data.json()

print(json_data)

# tree_widget = urwidtrees.widgets.TreeBox(
#     urwidtrees.decoration.CollapsibleIndentedTree(
#         urwidtrees.tree.SimpleTree([
#             (urwid.SelectableIcon('item 1'), (
#                 (urwid.SelectableIcon('sub item 1'), None),
#                 (urwid.SelectableIcon('sub item 2'), None),
#             )),
#             (urwid.SelectableIcon('item 2'), None),
#         ])
#     )
# )
#
# urwid.MainLoop(tree_widget).run()
