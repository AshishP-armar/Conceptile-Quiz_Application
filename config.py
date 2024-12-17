# config.py
import os

# Default DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_app_project.settings")

# Optional: Print confirmation (for debugging)
print(f"DJANGO_SETTINGS_MODULE is set to: {os.getenv('DJANGO_SETTINGS_MODULE')}")
