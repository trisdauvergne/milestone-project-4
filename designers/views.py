from django.shortcuts import render, redirect

from prints.forms import TestForm, TestPic

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


def all_designers_temp2(request):
    """ Temporary view for testing image upload """
    form = TestPic()
    if request.method == 'POST':
        form = TestPic(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_designers')
    else:
        form = TestPic()
    return render(request,
                  'designers/all_designers_temp2.html',
                  {'form': form})
