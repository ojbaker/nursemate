from django.db import models

# Create your models here.
class TaskItem(models.Model):
    content = models.TextField()
   # date_created = models.DateTimeField()
    # author = models.TextField