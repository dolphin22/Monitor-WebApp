from django.conf.urls import patterns, url

from .views import HTWListView, HTWCreateView, HTWUpdateView, HTWDeleteView

urlpatterns = patterns('',
			url(r'^$', HTWListView.as_view(), name='htw_list'),
			url(r'^add/$', HTWCreateView.as_view(), name='htw_create'),
			url(r'^(?P<pk>\d+)/$', HTWUpdateView.as_view(), name='htw_update'),
			url(r'^(?P<pk>\d+)/delete/$', HTWDeleteView.as_view(), name='htw_delete'),
		)
