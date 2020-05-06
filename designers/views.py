from django.shortcuts import render
from prints.models import Designer, Print

# Create your views here.


def all_designers(request):
    """ A view to return the all designers page """
    designers = Designer.objects.all()
    prints = Print.objects.all()

    context = {
        'designers': designers,
        'prints': prints,
    }

    return render(request,
                  'designers/all_designers.html',
                  context)

