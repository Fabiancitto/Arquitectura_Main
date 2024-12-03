from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def generar_gastos(request):
    return render(request, 'generar_gastos.html')

def pagar_gasto(request):
    return render(request, 'pagar_gasto.html')

def ver_pagos(request):
    return render(request, 'ver_pagos.html')
