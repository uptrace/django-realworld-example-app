#!/bin/bash

# Enable Django instrumentation.
export OTEL_DJANGO_INSTRUMENT=True

python3 manage.py runserver
