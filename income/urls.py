from django.urls import path
from .views import IncomeListView

urlpatterns = [
        path('', IncomeListView.as_view(), name='income_list'),
        ]
