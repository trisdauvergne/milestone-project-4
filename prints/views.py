from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import UploadPic

from .models import Print


def all_prints(request):
    """ A view to show all the prints on Planchest """
    prints = Print.objects.all()

    context = {
        'prints': prints,
    }

    return render(request,
                  'prints/all_prints.html',
                  context)


def single_print(request, print_id):
    """ A view to see a single print after its small version is clicked """
    the_print = get_object_or_404(Print, id=print_id)

    context = {
        'the_print': the_print,
    }

    return render(request,
                  'prints/single_print.html',
                  context)


@login_required
def add_print(request):
    """ A view where designers can add their prints to the site """
    form = UploadPic()
    if request.method == 'POST':
        form = UploadPic(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_prints')
    else:
        form = UploadPic()
    return render(request,
                  'prints/add_print.html',
                  {'form': form})



