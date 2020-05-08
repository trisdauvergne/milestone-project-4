from django.shortcuts import render

from .forms import Print


def all_prints(request):
    """ A view to show all the prints on Planchest """
    prints = Print.objects.all()

    context = {
        'prints': prints,
    }

    return render(request,
                  'prints/all_prints.html',
                  context)
