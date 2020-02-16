from django.shortcuts import render
from django.views.generic.edit import CreateView,FormView

from django.contrib.auth import authenticate, login


# Create your views here.
from .models import MyUser
from .forms import RegistrationFrom, LoginForm



class RegisterUser(FormView):
    """ view for regitsration """
    template_name = 'customuser/register.html'
    form_class = RegistrationFrom
    success_url= '/login/'


def login_user(request):
    """ view for login """

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email,password)
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                print("login success full ")
            else:
                print("invalid login ")
        else:
            form = LoginForm()


    return render(request, 'customuser/login.html', { 'form' : form })



