'''
Copyright (c) 2020 Gino Latorilla.
'''

import pytest
import subprocess
import os

from .testables import ninja_log_analyser


def test_must_be_executable_with_builtin_help():
    result = subprocess.run([ninja_log_analyser.__file__, '-h'])
    assert result.returncode == 0


def test_must_look_for_ninja_log_by_default_in_cwd(mocker):
    mocker.patch('ninja_log_analyser.argparse.open',
                 mocker.mock_open(read_data='# ninja log v5'))

    mocker.patch('ninja_log_analyser.sys.argv', ['__main__'])
    ninja_log_analyser.main()

    ninja_log_analyser.argparse.open.assert_has_calls([
        mocker.call(os.path.join(os.getcwd(), '.ninja_log'), 'r', mocker.ANY,
                    mocker.ANY, mocker.ANY),
        mocker.call().readline()
    ])


def test_accept_ninja_log_path_as_input(mocker):
    mocker.patch('ninja_log_analyser.argparse.open',
                 mocker.mock_open(read_data='# ninja log v5'))

    mocker.patch('ninja_log_analyser.sys.argv',
                 ['__main__', '-i', '/path/to/.ninja_log'])
    ninja_log_analyser.main()

    ninja_log_analyser.argparse.open.assert_has_calls([
        mocker.call('/path/to/.ninja_log', 'r', mocker.ANY, mocker.ANY,
                    mocker.ANY),
        mocker.call().readline()
    ])


def test_abort_when_ninja_log_missing_in_cwd(mocker):
    mocker.patch('ninja_log_analyser.argparse.open', side_effect=OSError)

    with pytest.raises(SystemExit):
        mocker.patch('ninja_log_analyser.sys.argv', ['__main__'])
        ninja_log_analyser.main()

    ninja_log_analyser.argparse.open.assert_called_once_with(
        os.path.join(os.getcwd(), '.ninja_log'), 'r', mocker.ANY, mocker.ANY,
        mocker.ANY)


def test_abort_when_ninja_log_missing_in_input_args(mocker):
    mocker.patch('ninja_log_analyser.argparse.open', side_effect=OSError)

    with pytest.raises(SystemExit):
        mocker.patch('ninja_log_analyser.sys.argv',
                     ['__main__', '-i', '/bogus/path'])
        ninja_log_analyser.main()

    ninja_log_analyser.argparse.open.assert_called_once_with(
        '/bogus/path', 'r', mocker.ANY, mocker.ANY, mocker.ANY)


def test_invalid_ninja_log_header(mocker):
    mocker.patch('ninja_log_analyser.argparse.open',
                 mocker.mock_open(read_data='R@nd0m 6aRbA63!!~'))

    with pytest.raises(SystemExit):
        mocker.patch('ninja_log_analyser.sys.argv', ['__main__'])
        ninja_log_analyser.main()

    ninja_log_analyser.argparse.open.assert_has_calls([
        mocker.call(os.path.join(os.getcwd(), '.ninja_log'), 'r', mocker.ANY,
                    mocker.ANY, mocker.ANY),
        mocker.call().readline()
    ])
