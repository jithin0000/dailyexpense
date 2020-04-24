from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models import Sum
from django.db.models.functions import TruncMonth
from datetime import date
import datetime
# Create your views here.

from income.models import Income
from expense.models import Expense

from django.db.models import Q
from django.http import JsonResponse

def home_graph(request):
        expense_by_month = (
            Expense.objects.filter().annotate(month=TruncMonth('created_on'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
                )

        income_by_month = (
            Income.objects.filter().annotate(month=TruncMonth('created_on'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
                )

        expense = [item for item in expense_by_month]  
        income = [item for item in income_by_month]  

        return JsonResponse(data={
                "expense" : expense, "income" : income
        },safe=False)

@login_required(login_url='/login')
def home(request):
    """ testing home view """

    income_sum = Income.objects.filter(user = request.user).aggregate(Sum('amount'))
    expense_sum = Expense.objects.filter(user = request.user).aggregate(Sum('amount'))
    
    today = date.today()
    todays_expense = todayExpenseFilter(request,today)

    todays_income = todayIncomeFilter(request, today)


    yesterday = date.today() - datetime.timedelta(days=1)


    yesterdays_expense = yesterdayExpenseFilter(request, yesterday)


    yesterdays_income = yesterdayIncomeFilter(request, yesterday)

    last_7_days = date.today() - datetime.timedelta(days=7)
    past_7_day_expense = weekExpenseFilter(request, last_7_days)
    past_7_day_income = weekIncomeFilter(request, last_7_days)

    this_month_expense = expenseMonthFilter(request, today)
    this_month_income = incom_month_filter(request, today)

   


    context_object = {
            'total_income' : income_sum['amount__sum'],
            'total_expense' : expense_sum['amount__sum'],
            'todays_expense' : todays_expense['amount__sum'],
            'todays_income' : todays_income['amount__sum'],
            'yesterdays_expense' : yesterdays_expense['amount__sum'],
            'yesterdays_income' : yesterdays_income['amount__sum'],
            'week_expense' : past_7_day_expense['amount__sum'],
            'week_income' : past_7_day_income['amount__sum'],
            'month_expense' : this_month_expense['amount__sum'],
            'month_income' : this_month_income['amount__sum'],
            }

    return render(request, 'home/home.html', context_object )


def todayExpenseFilter(request, today):
        return Expense.objects.filter(user = request.user).filter( Q(created_on__year = today.year) & Q(created_on__month = today.month) & Q(created_on__day = today.day)).aggregate(Sum('amount'))


def todayIncomeFilter(request, today):
        return Income.objects.filter(user = request.user).filter( Q(created_on__year = today.year) & Q(created_on__month = today.month) & Q(created_on__day = today.day)).aggregate(Sum('amount'))


def yesterdayExpenseFilter(request, yesterday):
        return Expense.objects.filter(user = request.user ).filter(
            Q(created_on__year = yesterday.year) & Q(created_on__month = yesterday.month) & Q(created_on__day = yesterday.day)
            ).aggregate(Sum('amount'))
def yesterdayIncomeFilter(request, yesterday):
        return Income.objects.filter(user = request.user ).filter( Q(created_on__year = yesterday.year) & Q(created_on__month = yesterday.month) & Q(created_on__day = yesterday.day) ).aggregate(Sum('amount'))

def weekExpenseFilter(request, last_7_days):
        return Expense.objects.filter( user = request.user ).filter(created_on__gte= last_7_days).aggregate(Sum('amount'))

def weekIncomeFilter(request, last_7_days):
        return Income.objects.filter( user = request.user ).filter(created_on__gte= last_7_days).aggregate(Sum('amount'))

def expenseMonthFilter(request, today):
        return Expense.objects.filter(user =request.user).filter( Q(created_on__year = today.year) & Q(created_on__month = today.month) ).aggregate(Sum('amount'))

def incom_month_filter(request, today):
        return Income.objects.filter(user =request.user).filter( Q(created_on__year = today.year) & Q(created_on__month = today.month) ).aggregate(Sum('amount'))
