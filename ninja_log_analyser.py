#!/usr/bin/env python3
'''ninja_log_analyser -- Reads a .ninja_log and ranks build times of objects.

Copyright (c) 2020 ginolatorilla
'''
import argparse
import sys
import os
import re
import logging


def main():
    program_options = get_program_options()
    header = program_options.input_file.readline()
    if re.match(r'^#\s+ninja\s+log\s+v\d+$', header) is None:
        logging.error('Not a valid .ninja_log (missing header)')
        sys.exit(1)
    return 0


def get_program_options():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i',
                        '--input-file',
                        help='Path to a .ninja_log file.',
                        default=os.path.join(os.getcwd(), '.ninja_log'),
                        type=argparse.FileType('r'))
    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main())
