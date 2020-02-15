from django.shortcuts import render

# Create your views here.


def home(request):
    """ testing home view """

    return render(request, 'home/home.html', {})
