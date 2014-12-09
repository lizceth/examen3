from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['usuario','telefono','documento','numero_doc','departamento','provincia','distrito','zona_horaria']
