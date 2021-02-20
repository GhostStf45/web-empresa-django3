from django.urls import path
from . import views

urlpatterns = [

     # normal user paths
    path('', views.blog, name='blog'),

    # path('.....<tipo_de_dato:params>')
    path('category/<int:category_id>/', views.category, name='category')

]