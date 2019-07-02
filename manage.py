#!/usr/bin/env python
import os
import sys

try:
    import settings.development
    MODE = 'development'
except ImportError:
    MODE = 'production'

def get_env():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.%s' % MODE)
    

if __name__ == "__main__":
    get_env()
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
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