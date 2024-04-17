# Python Packaging Reference

[![Build](https://github.com/alexandru-dinu/python-packaging/actions/workflows/main.yml/badge.svg)](https://github.com/alexandru-dinu/python-packaging/actions/workflows/main.yml)

Simple, no-hassle reference for packaging a Python project using just `pyproject.toml`.

## Usage

```console
$ python3 -m venv ./venv
$ source venv/bin/activate
$ pip3 install -e .
$ pip3 install -e ".[dev]"
```

If you want to use conda:
```console
$ conda create -n ENVNAME "python>=3.8" --file requirements.txt
```

## References
- https://til.simonwillison.net/python/pyproject
- https://stackoverflow.com/a/76722681
