from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from prints.models import Print
from django.contrib.auth.models import User


def all_designers(request):
    """ A view to return the all designers page """
    designer = User.objects.all()
    ordered_designers = designer.order_by('last_name')
    prints = Print.objects.all()

    context = {
        'designers': ordered_designers,
        'prints': prints,
    }

    return render(request,
                  'designers/all_designers.html',
                  context)


def designer_detail(request, designer_id):
    """ A view to return detail about a specific designer """
    the_designer = User.objects.get(id=designer_id)
    prints_by_designer = Print.objects.filter(designer=the_designer)

    context = {
        'designer': the_designer,
        'prints': prints_by_designer,
    }

    return render(request,
                  'designers/designer_detail.html',
                  context)


@login_required
def designer_profile(request):
    """ A view for users to create a designer profile to sell work """
    user_profile = User.objects.all()

    context = {
        'user': user_profile,
    }

    return render(request,
                  'designers/designer_profile.html',
                  context)
