from django.core.management import execute_from_command_line
from django.conf import settings
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

def main():
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
