from django.urls import path
from . import views

urlpatterns = [
    path('entrada/<int:autor_id>/', views.lista_entradas, name='lista_entradas'),
    path('', views.index, name='index'),
]
