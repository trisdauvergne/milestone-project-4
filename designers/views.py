from django.shortcuts import render

from prints.models import Print

from .models import Designers


def all_designers(request):
    """ A view to return the all designers page """
    designers = Designers.objects.all()
    prints = Print.objects.all()

    context = {
        'designers': designers,
        'prints': prints,
    }

    return render(request,
                  'designers/all_designers.html',
                  context)


def designer_detail(request):
    """ A view to return detail about a specific designer """
    designer = Designers.objects.get(pk=4)

    context = {
        'designer': designer,
    }

    return render(request,
                  'designers/designer_detail.html',
                  context)
