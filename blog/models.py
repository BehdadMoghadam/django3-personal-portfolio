from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    time = models.TimeField()
    date = models.DateField(blank = True)
