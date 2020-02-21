from django.urls import path
from .views import IncomeListView, IncomCreateView


urlpatterns = [
        path('', IncomeListView.as_view(), name='income_list'),
        path('new', IncomCreateView.as_view(), name='create_income')
        ]
