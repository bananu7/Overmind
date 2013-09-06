from django.conf.urls import patterns, url

from Lists import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ListDetailView.as_view(), name='detail'),
    url(r'^(?P<list_pk>\d+)/add/$', views.ListItemCreateView.as_view(), name='add'),
    url(r'^create/$', views.ListCreateView.as_view(), name='create'),
    url(r'^(?P<list_pk>\d+)/vote/(?P<item_pk>\d+)/$', views.VoteView.as_view(), name='vote'),
    url(r'^(?P<list_pk>\d+)/update_checks/$', views.updateChecks, name='update_checks'),
)
