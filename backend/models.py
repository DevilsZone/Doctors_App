from django.db import models
from django_extensions.db.fields import CreationDateTimeField

# Create your models here.
class AsyncResults(models.Model):
    task_id = models.CharField(blank=False, max_length=255, null=False, verbose_name="task id", db_index=True)
    result = models.TextField(blank=False, verbose_name="task result")
    created_on = CreationDateTimeField(db_index=True, editable=False, verbose_name="created_on")

