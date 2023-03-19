from django.db import models

# Create your models here.

class AboutMe(models.Model):
    paragraph_1 = models.CharField(max_length=1000)
    paragraph_2 = models.CharField(max_length=1000)
    paragraph_3 = models.CharField(max_length=1000)
    paragraph_4 = models.CharField(max_length=1000)
    paragraph_5 = models.CharField(max_length=1000, null=True, blank=True)
    paragraph_6 = models.CharField(max_length=1000, null=True, blank=True)