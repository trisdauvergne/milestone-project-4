from django import forms

from .models import Designer, Print


class TestForm(forms.ModelForm):

    class Meta:
        model = Designer
        fields = ('full_name',
                  'country',
                  'bio',
                  'email')


class TestPic(forms.ModelForm):

    class Meta:
        model = Print
        fields = ('designer',
                  'title',
                  'description',
                  'size',
                  'price',
                  'image')

