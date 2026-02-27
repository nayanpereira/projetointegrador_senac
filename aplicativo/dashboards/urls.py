from django.urls import path
from . import views 

urlpatterns = [
    path('dashboards/', views.abrir_dashboards, name='dashboards')
]