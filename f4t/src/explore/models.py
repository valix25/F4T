from django.db import models

# Create your models here.

class Feature(models.Model):
    feature_text = models.CharField(max_length=100)
    