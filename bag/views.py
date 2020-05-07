from django.shortcuts import render


def view_bag(request):
    """ A view to show all items in a shopping bag """
    return render(request, 'bag/view_bag.html')
