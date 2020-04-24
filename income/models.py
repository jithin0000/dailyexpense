from django.db import models

# Create your models here.
from customuser.models import MyUser

class Income(models.Model):
    """ model for income """

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
