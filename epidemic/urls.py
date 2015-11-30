from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^code/', views.code, name='code'),
    url(r'^model_description/', views.model_description, name='model_description'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]

