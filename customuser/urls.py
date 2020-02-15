from django.urls import path

from .views import index,RegisterUser


urlpatterns = [ 
        
        path('', RegisterUser.as_view(), name='register')

        ]
