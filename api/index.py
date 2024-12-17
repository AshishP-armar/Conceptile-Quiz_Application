import os
from django.core.wsgi import get_wsgi_application

# Set the settings module for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_app_project.settings")

# Expose the WSGI callable as 'app'
app = get_wsgi_application()