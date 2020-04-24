from django.contrib import admin

# Register your models here.
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_filter = ('created_on','amount')


admin.site.register(Expense, ExpenseAdmin)
