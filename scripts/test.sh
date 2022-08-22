#!/usr/bin/env bash

export PATH=env/bin:${PATH}

set -ex

pytest --verbose --cov plausible/ --cov-report term --cov-report html tests/

if hash black 2>/dev/null;
then
    black plausible tests setup.py --check
fi

flake8 plausible tests setup.py

isort -c plausible tests setup.py

mypy plausible tests setup.py
