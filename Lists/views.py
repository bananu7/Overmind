# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.forms import ModelForm
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

class ListCreateView(CreateView):
    model=List
    template_name = 'Lists/create_form.html'
    success_url = '/lists/'

class ListItemForm(ModelForm):
    class Meta:
        model = ListItem
        fields = ('title',)

class ListItemCreateView(CreateView):
    model = ListItem
    template_name = 'Lists/create_form.html'
    def get_success_url(self):
        return '/lists/%s/' % self.kwargs['list_pk']
    form_class = ListItemForm
    def post(self, request, *args, **kwargs):
        # Create empty item object
        item = ListItem()
        # Set parent list id
        item.parent_list = List.objects.get(pk=self.kwargs['list_pk'])
        # And creator
        item.user = request.user
        # Get the actual data sent with the form
        form = ListItemForm(request.POST, instance=item)
        # Save it to db
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




