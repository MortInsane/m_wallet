from django.db import models
from datetime import date


class Categories(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Accounting(models.Model):
    income_expense = models.CharField(max_length=7)
    description = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    created_date = models.DateField(default=date.today)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.description

