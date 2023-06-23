from django.shortcuts import render

def mostrar_info(request):
    return render(request, "informacion.html")

def panel_general(request):
    return render(request, "administrador/panel_general.html")

def sesiones(request):
    return render(request, "administrador/sesiones.html")

def entradas(request):
    return render(request, "administrador/entradas.html")