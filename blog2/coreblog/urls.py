from django.conf.urls import url

from . import views

app_name = 'coreblog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^edit/(\d+)$', views.edit, name='edit'),
    url(r'^add/$', views.new, name='new')
]