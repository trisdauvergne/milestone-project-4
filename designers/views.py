from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from prints.forms import TestForm

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


def all_designers_temp(request):
    """ Temporary view for testing forms """
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_designers')
    else:
        form = TestForm()
    return render(request,
                  'designers/all_designers_temp.html',
                  {'form': form})
