from django.shortcuts import render

# Create your views here.


def all_designers(request):
    """ A view to return the all designers page """
    return render(request, 'designers/all_designers.html')
