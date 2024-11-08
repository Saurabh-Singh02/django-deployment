"""
WSGI config for Portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

application = get_wsgi_application()

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def application(environ, start_response):
    try:
        # Your application logic here
        logging.info("Request received")
        # ... process the request ...
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [b"Internal Server Error"]
