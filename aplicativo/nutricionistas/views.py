from django.shortcuts import render

# O nome deve ser exatamente abrir_nutricionistas
def abrir_nutricionistas(request):
    return render(request, 'nutricionistas/index.html')