# -*- coding: utf-8 -*-

import json


def jsonformat(fp):
    data = json.load(fp)
    return json.dumps(data, indent=4)
