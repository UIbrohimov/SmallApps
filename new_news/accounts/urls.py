from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('signup/', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),
]