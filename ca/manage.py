#!/bin/bash

BASEDIR=/usr/local/share/django-ca
PYTHON=${BASEDIR}/bin/python
MANAGE=${BASEDIR}/ca/manage.py

${PYTHON} ${MANAGE} "$@"
