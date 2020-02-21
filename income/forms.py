from django import forms 

from .models import Income

class IncomeForm(forms.ModelForm):
    """ form for creating income """

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    amount =forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Income
        fields =['name','amount']
