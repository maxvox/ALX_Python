#!/bin/sh

pytest

pytest --cov

coverage report

coverage html
