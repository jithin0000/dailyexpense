from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from income.models import Income
# Create your views here.

class IncomeListView(LoginRequiredMixin,ListView):
    """ list view for income """
    model = Income
