#!/usr/bin/env python
import os
import sys

import uptrace
from opentelemetry.instrumentation.django import DjangoInstrumentor

from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conduit.settings")

    upclient = uptrace.Client()

    # This call is what makes the Django application be instrumented
    DjangoInstrumentor().instrument()
    Psycopg2Instrumentor().instrument()

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
