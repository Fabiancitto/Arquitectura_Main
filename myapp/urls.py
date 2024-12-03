from django.urls import path
from . import views

urlpatterns = [
    path('generar-gastos/', views.generar_gastos, name='generar_gastos'),
    path('pagar-gasto/', views.pagar_gasto, name='pagar_gasto'),
    path('ver-pagos/', views.ver_pagos, name='ver_pagos'),
]
