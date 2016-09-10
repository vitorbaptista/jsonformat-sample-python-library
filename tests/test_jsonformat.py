# -*- coding: utf-8 -*-

import pytest
import json
import jsonformat
from io import StringIO

try:
    unicode = unicode
except NameError:
    unicode = str


class TestJsonFormat(object):
    def test_returns_json_str_indented_with_4_whitespaces(self):
        data = {
            'foo': 'bar',
        }
        fp = StringIO(unicode(json.dumps(data)))

        assert jsonformat.jsonformat(fp) == json.dumps(data, indent=4)

    def test_invalid_json_raises_valueerror(self, tmpdir):
        fp = StringIO(unicode('invalid-json'))

        with pytest.raises(ValueError):
            jsonformat.jsonformat(fp)
