#!/usr/bin/env python
"""
manage.py - This is the ENTRY POINT of every Django project.
Think of it as the "remote control" for your project.
You use this file to:
  - Start the server (runserver)
  - Create the database tables (migrate)
  - Create an admin user (createsuperuser)
"""

import os        # os = Operating System. Used to set environment variables.
import sys       # sys = System. Used to read command-line arguments.

def main():
    # Tell Django which settings file to use
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you sure it's installed?") from exc
    
    # This runs whatever command you type, e.g. "runserver" or "migrate"
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
