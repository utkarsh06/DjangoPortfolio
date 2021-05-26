from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=400)