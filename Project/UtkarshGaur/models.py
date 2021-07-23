from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length= 100, default= "Default title")
    image = models.ImageField(upload_to = 'static/images/')
    summary = models.CharField(max_length=400)
