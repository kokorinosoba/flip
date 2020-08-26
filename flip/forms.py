from django import forms
from .models import Flip


class FlipForm(forms.ModelForm):


    class Meta:
        model = Flip
        fields = ('team_name', 'text')
