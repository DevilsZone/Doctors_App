import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Doctors_App.settings")
django.setup()

from backend.models import AsyncResults

def create_model(task_id, result):
    AsyncResults.objects.create(task_id=task_id, result=result)

def get_model(task_id):
    return AsyncResults.objects.get(task_id=task_id)