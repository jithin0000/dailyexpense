from django.urls import path

from home.views import home,home_graph


urlpatterns = [
        
        path('', home, name='home'),
        path('graph', home_graph, name='graph'),

        ]
