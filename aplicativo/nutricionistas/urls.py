from django.urls import path
from . import views 

urlpatterns = [
    # O views.abrir_nutricionistas deve apontar para a função acima
    path('nutricionistas/', views.abrir_nutricionistas, name='nutricionistas')
]