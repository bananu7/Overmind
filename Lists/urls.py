from django.conf.urls import patterns, url

from Lists import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ListDetailView.as_view(), name='detail'),
    url(r'^create/$', views.ListItemCreateView.as_view(), name='create'),
)
