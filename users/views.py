from django.shortcuts import render


def user_registration(request):
    """ A view to show the registration page """
    return render(request,
                  'users/user_registration.html')


def user_login(request):
    """ A view to show the login page"""
    return render(request,
                  'users/user_login.html')
