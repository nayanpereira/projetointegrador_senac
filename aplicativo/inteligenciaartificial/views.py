from django.shortcuts import render
# função para renderizar o questionário ;;
def abrir_ia(request):
    return render(request, 'inteligenciaartificial/index.html')# Create your views here.
