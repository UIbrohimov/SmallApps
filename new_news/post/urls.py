from django.conf.urls import url
from .import views

app_name = 'post'


urlpatterns = [
	url(r'^$', views.list_view, name='list_view'),
    url('create/', views.create_view, name='create'),
    url(r'^(?P<pk>\d+)/$', views.detail_view, name='detail'),
    # url(r'^(?P<slug>\w+)/$', views.detail_view, name='detail'),
] 