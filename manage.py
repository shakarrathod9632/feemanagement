#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feemanagement.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # ✅ Auto-create superuser on Render
    if os.environ.get("RENDER") == "true":
        import django
        django.setup()
        from django.contrib.auth import get_user_model
        
        User = get_user_model()
        username = "shankarrathod"
        password = "sakku@123"
        email = "sakku123@gmail.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print("✅ Superuser created on Render!")
        else:
            print("✅ Superuser already exists — skipping")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
