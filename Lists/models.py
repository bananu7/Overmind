from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length = 200)
    priority = models.IntegerField(default = 0)
    user = models.ForeignKey(User)

class ListItem(models.Model):
    checked = models.BooleanField()
    title = models.CharField(max_length = 400)
    parent_list = models.ForeignKey(List)

