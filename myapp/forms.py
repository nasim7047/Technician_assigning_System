from django import forms
from .models import Users
class Bal(forms.ModelForm):
    class meta:
        model=Users
        fields="__all__"