from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit/', views.edit_profile, name='edit_profile'),
]
