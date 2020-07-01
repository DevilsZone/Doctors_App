import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Doctors_App.settings")
django.setup()

from .models import get_model

x = get_model(task_id=1)