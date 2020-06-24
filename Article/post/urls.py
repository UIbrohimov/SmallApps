from django.conf.urls import url
from .import views

app_name = 'post'

urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url('about/', views.about_view, name='about'), 
    url(r'^(?P<pk>\w+)/$', views.detail_view, name='detail'),
]