#!/usr/bin/env python3
'''ninja_log_analyser -- Reads a .ninja_log and ranks build times of objects.

Copyright (c) 2020 ginolatorilla
'''
import argparse
import sys


def main():
    program_options = get_program_options()
    return 0


def get_program_options():
    parser = argparse.ArgumentParser(description=__doc__)
    return parser.parse_args()


if __name__ == '__main__':
    sys.exit(main())
