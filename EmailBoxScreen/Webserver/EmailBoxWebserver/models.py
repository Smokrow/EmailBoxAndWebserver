from django.db import models
from django import forms
class Nachricht(models.Model):
    Nachricht_text=models.TextField('Nachrichtentext')
    zeitstempel=models.FloatField()
    EmailAddresse=models.EmailField()
    Showen=models.BooleanField()
    zeitstring = models.CharField(max_length=100)

