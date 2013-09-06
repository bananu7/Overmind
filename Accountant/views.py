# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.forms import ModelForm
from Accountant.models import *

class IndexView(ListView):
    template_name = 'Accountant/spending_list.html'
    model = Spending
    context_object_name = 'spendings'
