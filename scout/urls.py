from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^parent/$', views.add_parent, name='parent-create'),
    url(r'^parent/(?P<pk>\d+)/$', views.ParentDetail.as_view(), name='parent-detail'),
    url(r'^ward/$', views.add_ward, name='ward-create'),
    url(r'^ward/(?P<pk>\d+)/$', views.WardDetail.as_view(), name='ward-detail'),
]
