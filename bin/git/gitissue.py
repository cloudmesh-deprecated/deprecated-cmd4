from __future__ import print_function

from pprint import pprint

import requests

from cloudmesh_client.common.util import banner

r = requests.get('https://api.github.com/repos/cloudmesh/client/issues')

issues = r.json()

pprint(issues)

for issue in issues:
    banner(issue["title"])
    if issue["milestone"] is not None:
        print(issue["milestone"]["title"])
    if issue["assignee"] is not None:
        print(issue["assignee"]["login"])
    for attribute in ["number",
                      "state",
                      "title",
                      "body"]:
        if issue[attribute]:
            print(attribute, ":", issue[attribute])
