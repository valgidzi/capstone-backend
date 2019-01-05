from django.db import models
from textstat import textstat

# Create your models here.

class Material(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=False)
    level = models.CharField(max_length=2, blank=False)

class Text(models.Model):
    original = models.TextField()
    score = models.CharField(max_length=200, default='Not calculated')

    def level_score(self):
        return textstat.text_standard(self.original)
