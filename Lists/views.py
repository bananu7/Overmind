# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from Lists.models import *

class IndexView(ListView):
    template_name = 'Lists/index.html'
    context_object_name = 'lists'
    model = List

class ListDetailView(DetailView):
    context_object_name = 'list'
    model = List
    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['items'] = ListItem.objects.filter(parent_list = context["list"].id)
        return context

class ListItemCreateView(CreateView):
    model = ListItem 
    success_url = '/lists/'

