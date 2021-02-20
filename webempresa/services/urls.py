from django.urls import path
from . import views

urlpatterns = [

     # normal user paths
    path('', views.services, name='services'),

]