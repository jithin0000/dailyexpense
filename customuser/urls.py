from django.urls import path

from .views import RegisterUser


urlpatterns = [ 
        
        path('', RegisterUser.as_view(), name='register')

        ]
