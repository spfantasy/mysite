from django.conf.urls import url
from django.contrib import admin
from basic_app import views

# TEMPLATE TAGGING
app_name = "basic_app"

urlpatterns = [
    url(r'^registration', views.register, name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/', views.special, name='special'),
    url(r'^login/', views.user_login, name='login'),
]
