from django.db import models

# Create your models here.

class Handout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    words = models.TextField()
    word_order = models.TextField()
    definitions = models.TextField()
    definitions_order = models.TextField()
