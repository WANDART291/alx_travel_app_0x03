# alx_travel_app/celery.py

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

# Create a Celery instance. The argument is the name of the Celery app.
app = Celery('alx_travel_app')

# Load configuration from Django settings.
# namespace='CELERY' means all Celery-related settings must start with 'CELERY_' 
# in settings.py (e.g., CELERY_BROKER_URL).
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover task modules in all installed Django apps. 
# It looks for a tasks.py file in every app listed in INSTALLED_APPS.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    """Simple task to test if the worker is running and configured correctly."""
    print(f'Request: {self.request!r}')