from django.urls import path
from . import views


urlpatterns = [


    path('', views.logar_foto, name='logar'),
    path('deslogar', views.deslogar, name='deslogar'),

]