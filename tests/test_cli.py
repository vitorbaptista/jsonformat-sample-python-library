# -*- coding: utf-8 -*-

import subprocess
import json


class TestCLI(object):
    def test_prints_json_str_indented_with_4_whitespaces(self, capfd, tmpdir):
        data = {
            'foo': 'bar',
        }
        json_file = tmpdir.join('data.json')
        json_file.write(json.dumps(data))
        path = str(json_file.realpath())

        subprocess.call(['jsonformat', path])

        out, err = capfd.readouterr()
        assert out == ('%s\n' % json.dumps(data, indent=4))
        assert not err

    def test_inexistent_file_raises_error(self, capfd):
        path = 'inexistent-file.json'
        exit_code = subprocess.call(['jsonformat', path])

        out, err = capfd.readouterr()
        expected_message = (
            'Could not open file: {path}: No such file or directory\n'
        ).format(path=path)

        assert not out
        assert err.endswith(expected_message)
        assert exit_code != 0

    def test_invalid_json_raises_error(self, capfd, tmpdir):
        json_file = tmpdir.join('data.json')
        json_file.write('foobar')
        path = str(json_file.realpath())

        exit_code = subprocess.call(['jsonformat', path])

        out, err = capfd.readouterr()
        assert not out
        assert err == 'Error: {path} is not a valid JSON\n'.format(path=path)
        assert exit_code != 0
