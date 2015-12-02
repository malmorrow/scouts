from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^parent/$', views.CreateParent.as_view(), name='parent-create'),
    url(r'^parent/(?P<pk>\d+)/$', views.ParentDetail.as_view(), name='parent-detail'),
    url(r'^ward/$', views.CreateWard.as_view(), name='ward-create'),
    url(r'^ward/(?P<pk>\d+)/$', views.WardDetail.as_view(), name='ward-detail'),
]
