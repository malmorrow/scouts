from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parent_create/$', views.CreateParent.as_view(template_name="scout/parent_create.html"), name='parent_create'),
    url(r'parent/(?<parent_id>[0-9]+)/$', views.ParentDetail.as_view(template_name="scout/parent_detail.html")),
    url(r'^ward_create/$', views.CreateWard.as_view(template_name="scout/ward_create.html")),
    url(r'^(?P<ward_id>[0-9]+)/$', views.ward, name='ward'),
    url(r'^(?P<ward_id>[0-9]+)/update/$', views.update, name='update'),
]
