from django.db import models
from django.forms import ModelForm


# Create your models here.


class DietModel(models.Model):
    Female = 'F'
    Male = 'M'
    GENDER_CHOICES = [(Female, 'Female'), (Male, 'Male')]

    Full_name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=Female)
    Mobile_number = models.CharField(max_length=255)
    E_mail = models.EmailField()
    Fecal_sample = models.FileField(null=False)
