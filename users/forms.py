from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    """ A custom signup form with additional fields """
    first_name = forms.CharField(max_length=30,
                                 label='First Name')
    last_name = forms.CharField(max_length=30,
                                label='Last Name')
    country = forms.CharField(max_length=30,
                              label='Country')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.country = self.cleaned_data['country']
        user.save()
        return user
