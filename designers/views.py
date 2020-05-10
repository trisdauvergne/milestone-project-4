from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from prints.models import Print
from users.models import DesignerProfile
from django.contrib.auth.models import User

from users.forms import DesignerProfileForm


def all_designers(request):
    """ A view to return the all designers page """
    all_designers = DesignerProfile.objects.all()
    ordered_designers = all_designers.order_by('last_name')
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
    designer_profile_info = DesignerProfile.objects.get(id=designer_id)
    prints_by_designer = Print.objects.filter(designer=the_designer)

    context = {
        'designer': the_designer,
        'prints': prints_by_designer,
        'info': designer_profile_info,
    }

    return render(request,
                  'designers/designer_detail.html',
                  context)


def designer_profile(request, designer_id):
    """ A view for users to create a designer profile to sell work """
    the_designer = User.objects.get(id=designer_id)

    context = {
        'designer': the_designer,
    }

    return render(request,
                  'designers/designer_profile.html',
                  context)


def create_designer_profile(request, user_id):
    """ A view for a user to create a profile as a designer """
    # the_user = get_object_or_404(User, id=user_id)
    form = DesignerProfileForm()
    if request.method == 'POST':
        form = DesignerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_designers')
    else:
        form = DesignerProfileForm()
    return render(request,
                  'designers/create_designer_profile.html',
                  {'form': form})


def edit_designer_profile(request, designer_id):
    """ A view for designers to edit their user profile """
    designer = get_obj
    form = DesignerProfileForm()
    if request.method == 'POST':
        form = DesignerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_designers')

    return render(request,
                  'designers/edit_designer_profile.html')
