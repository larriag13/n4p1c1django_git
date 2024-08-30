from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pagina3/', views.pagina3),
]