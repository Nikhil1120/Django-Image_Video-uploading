from django.forms import fields 
from app1.models import Person
from django.forms import ModelForm
from django import forms

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields="__all__"
