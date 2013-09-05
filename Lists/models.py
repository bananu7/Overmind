from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.title

class ListItem(models.Model):
    checked = models.BooleanField(default=False)
    title = models.CharField(max_length = 400)
    parent_list = models.ForeignKey(List)
    user = models.ForeignKey(User)
    priority = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.title

