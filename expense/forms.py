from django import forms

from .models import Expense


class ExpenseForm(forms.ModelForm):
    """ form for create expense """

    class Meta:
        model = Expense
        fields =['name', 'amount']
