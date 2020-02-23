from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Expense 
from django.urls import reverse_lazy
from .forms import ExpenseForm

class ExpenseListView(LoginRequiredMixin,ListView):
    """ list view for expense """
    model = Expense

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class ExpenseCreateView(LoginRequiredMixin,CreateView):
    """ expense create view """
    form_class=ExpenseForm
    template_name='expense/expense_form.html'

    def form_valid(self, form, *args, **kwargs):
        """ add user to user field """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('expense_home')




