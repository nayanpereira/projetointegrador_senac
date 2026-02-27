from django.shortcuts import render

def abrir_treino(request):
    return render(request, 'personaltrainner/index.html')
