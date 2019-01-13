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
        score = textstat.text_standard(self.original)
        grade = int(score[0])
        if grade == 0 or grade == 1:
            return "A1"
        elif grade == 2 or grade == 3:
            return "A2"
        elif grade == 4 or grade == 5:
            return "B1"
        elif grade == 6 or grade == 7:
            return "B2"
        elif grade == 8 or grade == 9:
            return "C1"
        elif grade == 10 or grade == 11:
            return "C2"

class Handout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    words = models.TextField()
    word_order = models.TextField()
    definitions = models.TextField()
    definitions_order = models.TextField()
