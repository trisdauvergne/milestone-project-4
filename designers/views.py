from django.shortcuts import render

from prints.models import Print

from .models import Designers


def all_designers(request):
    """ A view to return the all designers page """
    designer = Designers.objects.all()
    designers = designer.order_by('full_name')
    prints = Print.objects.all()

    context = {
        'designers': designers,
        'prints': prints,
    }

    return render(request,
                  'designers/all_designers.html',
                  context)


def designer_detail(request, designer_id):
    """ A view to return detail about a specific designer """
    designer = Designers.objects.get(id=designer_id)
    prints = Print.objects.filter(designer=designer)

    context = {
        'designer': designer,
        'prints': prints,
    }

    return render(request,
                  'designers/designer_detail.html',
                  context)
