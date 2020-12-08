#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'front.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    
    import django
    import os
    django.setup()

    # Override default port for `runserver` command
    from django.core.management.commands.runserver import Command as runserver
    port = int(os.environ.get("PORT", 5000))
    runserver.default_port = port

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)