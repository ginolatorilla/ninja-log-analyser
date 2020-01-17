# Ninja Log Analyser

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ginolatorilla/ninja-log-analyser/Python%20application/master?style=for-the-badge)

Reads a `.ninja_log` and ranks build time of objects.

`.ninja_log` is produced by the [Ninja build system](https://ninja-build.org/manual.html#ref_log).

## Features

- Ranks objects in decreasing build time
- Can show times in milliseconds or seconds

## Requirements

- Python 3.6 or better

## Quick Start

Let there be a `.ninja_log` in the current working directory with the following contents:

```text
# ninja log v5
28339	37316	1568970682	a.o	21551924de56a0b0
21092	28683	1568970674	b.o	e5c447592b0f338f
10	1535	1568970647	libc.a	fec6486ac4c258a0
```

Run:

```bash
./ninja_log_analyser.py

# Similarly,
./ninja_log_analyser.py -i .ninja_log
```

Output:

```text
8977ms a.o
7591ms b.o
1525ms libc.a
```

## Development

You need to install [Pipenv](https://pipenv.readthedocs.io/en/latest/) first.

Run `./bootstrap-dev` to install requirements

Run `pipenv run pytest` to run all tests.
