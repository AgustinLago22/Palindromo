
from django.contrib import admin
from django.urls import path
from checker_palindromo.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido , name='bienvenido'),
    path('verificador', verificador, name = 'verificador'),
    path('verificador/create', created_at, name = 'create'),
    path('verificador/delete/<int:code>', delete_at, name = 'delete'),
    path('verificador/update/<int:code>', update_at, name = 'update'),
    path('verificador/verification/<int:code>', verification, name = 'verification'),

]
