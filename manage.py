#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # times = 1
    configuration='arqui.settings'
    os.environ['DJANGO_SETTINGS_MODULE']=configuration
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # try:
    #     os.environ['DJANGO_SETTINGS_MODULE']=configuration
    #     execute_from_command_line(sys.argv)
    # except: 
    #     pass
    # while times <= 3:
    #     if times==1:
    #         configuration='arqui.settings'
    #     elif times==2:
    #         configuration='arqui.pi_settings'
    #     else:
    #         configuration='arqui.local_settings'
    #     try:
    #         os.environ['DJANGO_SETTINGS_MODULE']=configuration
    #         execute_from_command_line(sys.argv)
    #     except: 
    #         pass
        # times+=1


if __name__ == '__main__':
    main()
