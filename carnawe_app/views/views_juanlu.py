from django.shortcuts import render


def mostrar_ajustesUser(request):
    return render(request, "ajustesUser.html")

def cambio_ajustesUser(request):
    return render(request, "modificar_Perfil.html")

def cambio_passwd(request):
    return render(request, "cambioPassword.html")