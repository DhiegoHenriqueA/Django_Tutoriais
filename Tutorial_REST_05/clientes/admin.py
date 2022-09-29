from django.contrib import admin

# Register your models here.
# clientes/admin.py
from django.contrib import admin
from .models import Cliente
admin.site.register(Cliente)