from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pagina2/', views.pagina2),
]