'''
Copyright (c) 2020 Gino Latorilla.
'''

import pytest
import subprocess

from .testables import ninja_log_analyser


def test_must_be_executable():
    assert subprocess.run(ninja_log_analyser.__file__).returncode == 0


def test_must_be_executable_with_builtin_help():
    result = subprocess.run([ninja_log_analyser.__file__, '-h'])
    assert result.returncode == 0
