from django.urls import path

from .views import RegisterUser, login_user


urlpatterns = [ 
        
        path('', RegisterUser.as_view(), name='register'),
        path('login', login_user, name='login')

        ]
