from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models import Sum
from datetime import date
import datetime
# Create your views here.

from income.models import Income
from expense.models import Expense

@login_required(login_url='/login')
def home(request):
    """ testing home view """

    income_sum = Income.objects.filter(user = request.user).aggregate(Sum('amount'))
    expense_sum = Expense.objects.filter(user = request.user).aggregate(Sum('amount'))
    

    todays_expense = Expense.objects.filter(
            created_on__year= date.today().year,
            created_on__month= date.today().month,
            created_on__day= date.today().day,
            ).aggregate(Sum('amount'))

    yesterday = date.today() - datetime.timedelta(days=1)

    yesterdays_expense = Expense.objects.filter(
            created_on__year = yesterday.year, created_on__month = yesterday.month, created_on__day = yesterday.day
            ).aggregate(Sum('amount'))

    context_object = {
            'total_income' : income_sum['amount__sum'],
            'total_expense' : expense_sum['amount__sum'],
            'todays_expense' : todays_expense['amount__sum'],
            'yesterdays_expense' : yesterdays_expense['amount__sum'],
            }

    return render(request, 'home/home.html', context_object )
