from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models import Sum
# Create your views here.

from income.models import Income
from expense.models import Expense

@login_required(login_url='/login')
def home(request):
    """ testing home view """

    income_sum = Income.objects.filter(user = request.user).aggregate(Sum('amount'))
    expense_sum = Expense.objects.filter(user = request.user).aggregate(Sum('amount'))
    context_object = {
            'total_income' : income_sum['amount__sum'],
            'total_expense' : expense_sum['amount__sum']
            }

    return render(request, 'home/home.html', context_object )
