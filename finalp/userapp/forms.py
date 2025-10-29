from django import forms
from .models import *

class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class notesform(forms.ModelForm):
    class Meta:
        model=note
        fields=['title','category','notesfile','Desc']

class cform(forms.ModelForm):
    class Meta:
        model=cntc
        fields='__all__'
