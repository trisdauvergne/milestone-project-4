from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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


@login_required
def add_print(request):
    """ A view where designers can add their prints to the site """

    return render(request,
                  'prints/add_print.html')
