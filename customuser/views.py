from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,FormView

from django.contrib.auth import authenticate, login, logout


# Create your views here.
from .models import MyUser
from .forms import RegistrationFrom, LoginForm


def register_user(request):
    """ register functional view """

    form = RegistrationFrom()

    if request.method == 'POST':
        form = RegistrationFrom(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = RegistrationFrom()


    return render(request,'customuser/register.html', {'form' : form})



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
                return redirect('home')
            else:
                print("invalid login ")
        else:
            form = LoginForm()


    return render(request, 'customuser/login.html', { 'form' : form })

def exit_to_app(request):
    """ log out view """
    logout(request)
    return redirect('register')
