from django.contrib import admin

# Register your models here.
from . models import Genero, Manga, Mangaka,Marca,Figuras,Tipo,Receta

admin.site.register(Manga)
admin.site.register(Mangaka)
admin.site.register(Genero)
admin.site.register(Figuras)
admin.site.register(Marca)
admin.site.register(Tipo)
admin.site.register(Receta)