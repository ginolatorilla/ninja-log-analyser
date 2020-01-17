#!/usr/bin/env python3
'''ninja_log_analyser -- Reads a .ninja_log and ranks build times of objects.

Copyright (c) 2020 ginolatorilla
'''
import argparse
import sys
import os
import re
import logging
import itertools


def main():
    program_options = get_program_options()
    header = program_options.input_file.readline()
    if re.match(r'^#\s+ninja\s+log\s+v\d+$', header) is None:
        logging.error('Not a valid .ninja_log (missing header)')
        sys.exit(1)

    parser = re.compile(
        r'^(?P<start>\d+)\s+(?P<end>\d+)\s+\d+\s+(?P<object>.+)\s+[\da-f]+$')

    def yield_parsed_line(parser, raw):
        match = parser.match(raw)
        if match is None:
            return {}
        else:
            return match.groupdict()

    document = ({
        'line': n + 1,
        **(yield_parsed_line(parser, l))
    } for n, l in enumerate(program_options.input_file.readlines()))

    def merge_computed_time(entry):
        if 'start' in entry and 'end' in entry:
            return {**entry, 'time': int(entry['end']) - int(entry['start'])}
        else:
            return entry

    m1, m2 = itertools.tee(merge_computed_time(i) for i in document)
    filtered = (i for i in m1 if 'object' in i)
    errors = (i['line'] for i in m2 if 'object' not in i)

    sys.stderr.write('\n'.join('warning: cannot parse line #{}'.format(e)
                               for e in errors) + '\n')
    print('\n'.join(
        '{0[time]}ms {0[object]}'.format(i)
        for i in sorted(filtered, key=lambda x: x['time'], reverse=True)))
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
