from django.contrib import admin
from holamundo.models import Libros

# Register your models here.
class AdminLibros(admin.ModelAdmin):
    model = Libros
    list_display=["nombre", "autor"]

admin.site.register(Libros, AdminLibros)