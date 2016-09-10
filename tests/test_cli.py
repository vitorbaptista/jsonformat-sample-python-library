# -*- coding: utf-8 -*-

import os
import subprocess
import json


class TestCLI(object):
    def test_prints_json_str_indented_with_4_whitespaces(self, capfd, tmpdir):
        data = {
            'foo': 'bar',
        }
        expected_output = _universal_newlines(json.dumps(data, indent=4))
        json_file = tmpdir.join('data.json')
        json_file.write(json.dumps(data))
        path = str(json_file.realpath())

        subprocess.call(['jsonformat', path])

        out, err = capfd.readouterr()
        assert _universal_newlines(out.strip()) == expected_output
        assert not err

    def test_inexistent_file_raises_error(self, capfd):
        path = 'inexistent-file.json'
        exit_code = subprocess.call(['jsonformat', path])

        out, err = capfd.readouterr()
        expected_message = (
            'Could not open file: {path}: No such file or directory'
        ).format(path=path)

        assert not out
        assert err.strip().endswith(expected_message)
        assert exit_code != 0

    def test_invalid_json_raises_error(self, capfd, tmpdir):
        json_file = tmpdir.join('data.json')
        json_file.write('foobar')
        path = str(json_file.realpath())

        exit_code = subprocess.call(['jsonformat', path])

        out, err = capfd.readouterr()
        expected_message = (
            'Error: {path} is not a valid JSON'
        ).format(path=path)

        assert not out
        assert err.strip() == expected_message
        assert exit_code != 0


def _universal_newlines(string):
    return string.replace(os.linesep, '\n')
