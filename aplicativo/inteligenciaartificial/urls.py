from django.urls import path
from . import views 

urlpatterns = [
    path('ia/', views.abrir_ia, name='ia')
]