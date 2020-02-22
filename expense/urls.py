from django.urls import path

from .views import ExpenseListView, ExpenseCreateView



urlpatterns = [
        
        path('', ExpenseListView.as_view(), name='expense_home'),
        path('new', ExpenseCreateView.as_view(), name='expense_create')


        ]
