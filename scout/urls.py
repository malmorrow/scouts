from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^parent_create/$', views.CreateParent.as_view(), name='parent-create'),
    url(r'^parent/(?P<pk>\d+)/$', views.ParentDetail.as_view(), name='parent-detail'),
    url(r'^ward_create/$', views.CreateWard.as_view(), name='ward-create'),
]
