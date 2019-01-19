from django.db import models

# Create your models here.

class Handout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    words = models.TextField()
    definitions = models.TextField()
    user = models.TextField()
    score = models.TextField()
    title = models.TextField()
