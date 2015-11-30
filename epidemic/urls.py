from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^test/', views.test, name='test'),
    url(r'^carousel/', views.carousel, name='carousel'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]

