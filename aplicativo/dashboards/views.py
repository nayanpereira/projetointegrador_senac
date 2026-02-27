from django.shortcuts import render

def abrir_dashboards(request):
    return render(request, 'dashboards/index.html')