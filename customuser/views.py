from django.shortcuts import render

from django.views.generic.edit import CreateView,FormView


# Create your views here.
from .models import MyUser
from .forms import RegistrationFrom


def index(request):
    return render(request, 'customuser/index.html', {})


class RegisterUser(FormView):
    """ view for regitsration """
    template_name = 'customuser/register.html'
    form_class = RegistrationFrom
    success_url= '/home/'
