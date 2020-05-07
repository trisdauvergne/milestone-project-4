from django.shortcuts import render


def all_prints(request):
    """ A view to show all the prints on Planchest """
    return render(request,
                  'prints/all_prints.html')
