from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models import Sum
from datetime import date
import datetime
# Create your views here.

from income.models import Income
from expense.models import Expense

from django.db.models import Q

@login_required(login_url='/login')
def home(request):
    """ testing home view """

    income_sum = Income.objects.filter(user = request.user).aggregate(Sum('amount'))
    expense_sum = Expense.objects.filter(user = request.user).aggregate(Sum('amount'))
    
    today = date.today()
    todays_expense = Expense.objects.filter(user = request.user).filter( Q(created_on__year = today.year) & Q(created_on__month = today.month) & Q(created_on__day = today.day)).aggregate(Sum('amount'))

    todays_income = Income.objects.filter( user = request.user ).filter(
            Q(created_on__year = today.year) & Q(created_on__month = today.month) & Q(created_on__day = today.day)
            ).aggregate(Sum('amount'))


    yesterday = date.today() - datetime.timedelta(days=1)


    yesterdays_expense = Expense.objects.filter(user = request.user ).filter(
            Q(created_on__year = yesterday.year) & Q(created_on__month = yesterday.month) & Q(created_on__day = yesterday.day)
            ).aggregate(Sum('amount'))


    yesterdays_income = Income.objects.filter(user = request.user ).filter(
            Q(created_on__year = yesterday.year) & Q(created_on__month = yesterday.month) & Q(created_on__day = yesterday.day)
            ).aggregate(Sum('amount'))

    last_7_days = date.today() - datetime.timedelta(days=7)
    past_7_day_expense = Expense.objects.filter( user = request.user ).filter(created_on__gte= last_7_days).aggregate(Sum('amount'))
    past_7_day_income = Income.objects.filter( user = request.user ).filter(created_on__gte= last_7_days).aggregate(Sum('amount'))

    this_month_expense = Expense.objects.filter(user =request.user).filter(
            Q(created_on__year = today.year) & Q(created_on__month = today.month)
            ).aggregate(Sum('amount'))
    this_month_income = Income.objects.filter(user =request.user).filter(
            Q(created_on__year = today.year) & Q(created_on__month = today.month)
            ).aggregate(Sum('amount'))


    context_object = {
            'total_income' : income_sum['amount__sum'],
            'total_expense' : expense_sum['amount__sum'],
            'todays_expense' : todays_expense['amount__sum'],
            'todays_income' : todays_income['amount__sum'],
            'yesterdays_expense' : yesterdays_expense['amount__sum'],
            'yesterdays_income' : yesterdays_income['amount__sum'],
            'week_expense' : past_7_day_expense['amount__sum'],
            'week_expense' : past_7_day_expense['amount__sum'],
            'month_expense' : this_month_expense['amount__sum'],
            'month_income' : this_month_income['amount__sum'],
            }

    return render(request, 'home/home.html', context_object )
