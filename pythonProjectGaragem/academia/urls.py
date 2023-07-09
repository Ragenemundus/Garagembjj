from django.urls import path
from . import views


urlpatterns = [


    path('', views.academia, name='academia'),

]