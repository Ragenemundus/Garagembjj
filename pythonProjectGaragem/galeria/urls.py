from django.urls import path
from . import views


urlpatterns = [


    path('', views.galeria, name='galeria'),
    path('subir', views.galeria_subir, name='subir'),
    path('apagar/<int:pk>/', views.apagar, name='apagar'),
    path('deletar/<int:pk>/', views.deletar, name='deletar'),
]
