from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Spending(models.Model):
    amount = models.IntegerField()
    creator = models.ForeignKey(User)
    title = models.CharField(max_length = 120)

class Payment(models.Model):
    user = models.ForeignKey(User)
    paid_amount = models.IntegerField()
    due_amount = models.IntegerField()
    spending = models.ForeignKey(Spending)
