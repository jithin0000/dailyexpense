from django.shortcuts import render

# Create your views here.
from .models import MyUser


def index(request):
    return render(request, 'customuser/index.html', {})
