from django.shortcuts import render


def usuarios(request):
    return render(request, "administrador/usuarios.html")

def agrupaciones(request):
    return render(request, "administrador/agrupaciones.html")


