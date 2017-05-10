
from django.db import models

# Create your models here.
from django.db import models
from django import forms
class Nachricht(models.Model):
    Nachricht_text=models.TextField('Nachrichtentext')
    zeitstempel=models.FloatField()
    EmailAddresse=models.EmailField()
    Showen=models.BooleanField()
    zeitstring = models.CharField(max_length=100)

class Addresse_Predef(models.Model):
    EmailAddresse = models.EmailField()
    Color_R=models.IntegerField()
    Color_G=models.IntegerField()
    Color_B = models.IntegerField()

