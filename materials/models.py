from django.db import models

# Create your models here.

class Material(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=False)
    level = models.CharField(max_length=2, blank=False)
