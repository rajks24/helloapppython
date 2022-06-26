import os
import json


def server_info():
    # printing environment variables
    envlist = {}
    for k, v in sorted(os.environ.items()):
        if "NODE_" in k or "POD_" in k:
            envlist[k] = v
    return envlist
