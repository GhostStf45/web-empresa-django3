from django.urls import path
from . import views

urlpatterns = [

    # path('.....<tipo_de_dato:params>')
    path('<int:page_id>/<slug:page_slug>', views.page, name='page')

]