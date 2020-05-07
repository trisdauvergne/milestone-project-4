from django import forms

from .models import Designer


class TestForm(forms.ModelForm):

    class Meta:
        model = Designer
        fields = ('full_name',
                  'country',
                  'bio',
                  'email')

