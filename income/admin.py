from django.contrib import admin

# Register your models here.
from .models import Income

class IncomAdmin(admin.ModelAdmin):

    list_filter = ("created_on",)
admin.site.register(Income, IncomAdmin)
