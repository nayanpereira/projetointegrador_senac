from django.urls import path
from . import views 

urlpatterns = [
    path('treino/', views.abrir_treino, name='treino')
]