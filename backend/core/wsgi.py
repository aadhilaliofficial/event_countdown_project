"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

if os.environ.get('VERCEL') == '1':
    from django.core.management import call_command
    from django.contrib.auth import get_user_model
    
    try:
        call_command('migrate', interactive=False)
        User = get_user_model()
        if not User.objects.filter(username='aadhilali').exists():
            User.objects.create_superuser('aadhilali', 'admin@example.com', 'aadhilali')
    except Exception as e:
        print(f"Startup error: {e}")
