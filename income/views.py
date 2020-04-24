from django.shortcuts import render,redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import IncomeForm

from income.models import Income
# Create your views here.

class IncomeListView(LoginRequiredMixin,ListView):
    """ list view for income """
    model = Income

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class IncomCreateView(LoginRequiredMixin, CreateView):
    """ create view for income """
    form_class = IncomeForm
    template_name="income/income_form.html"
    success_url=reverse_lazy('income_list')

    def form_valid(self, form,*args, **kwargs):
        self.object=form.save(commit=False)
        self.object.user =self.request.user
        self.object.save()
        return redirect(self.get_success_url())


