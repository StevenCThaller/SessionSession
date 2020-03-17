from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('setx', views.setthings),
    path('showx', views.showthings),
    path('clearsession', views.logout)
]