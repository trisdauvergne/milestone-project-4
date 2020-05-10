# from allauth.account.forms import SignupForm
from django import forms

from .models import DesignerProfile


# class CustomSignupForm(SignupForm):
#     """ A custom signup form with additional fields """
#     first_name = forms.CharField(max_length=30,
#                                  label='First Name')
#     last_name = forms.CharField(max_length=30,
#                                 label='Last Name')

#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()
#         return user

class DesignerProfileForm(forms.ModelForm):

    class Meta:
        model = DesignerProfile
        fields = ['user',
                  'first_name',
                  'last_name',
                  'country',
                  'bio']
