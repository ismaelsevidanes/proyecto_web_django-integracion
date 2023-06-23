from django.shortcuts import render

def mostrar_compraEntradas(request):
    return render(request,"compraEntradas.html")

def mostrar_pagoEntradas(request):
    return render(request,"pagoEntradas.html")

def mostrar_loginPago(request):
    return render(request,"loginPago.html")