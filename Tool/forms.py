from django.forms import ModelForm
from .models import DietModel
from django import forms


class DietForm(forms.ModelForm):
    class Meta:
        model = DietModel
        fields = '__all__'
