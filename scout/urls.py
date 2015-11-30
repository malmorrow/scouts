from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apply/$', views.apply, name='apply'),
    url(r'^(?P<ward_id>[0-9]+)/$', views.ward, name='ward'),
    url(r'^(?P<ward_id>[0-9]+)/update/$', views.update, name='update'),
]
