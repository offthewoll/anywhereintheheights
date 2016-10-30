from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^create-guest-account/', views.guest, name='guest'),
    url(r'^create-host-account/', views.host, name='host'),
]
