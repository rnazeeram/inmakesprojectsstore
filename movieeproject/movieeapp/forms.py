from django import forms
from .models import moviee
class movieForm(forms.ModelForm):
    class Meta:
        model=moviee
        fields=['name','desc','year','img']
