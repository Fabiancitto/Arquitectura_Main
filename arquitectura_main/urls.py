from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),  # Página raíz
    path('admin/', admin.site.urls),  # Admin site
    path('api/', include('myapp.urls')),  # Incluir las URLs de tu app
]
