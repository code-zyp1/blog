"""
WSGI config for untitled10 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/usr/local/python3/lib/python3.6/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled10.settings')

application = get_wsgi_application()
