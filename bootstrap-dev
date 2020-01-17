#!/usr/bin/env python3

'''
Copyright (c) 2019 Gino Latorilla.
'''

import subprocess
import os

env = os.environ.copy()
env['PIPENV_VENV_IN_PROJECT'] = '1'
subprocess.run('pipenv --python 3 --three'.split(), env=env)
subprocess.run('pipenv install --dev'.split())
