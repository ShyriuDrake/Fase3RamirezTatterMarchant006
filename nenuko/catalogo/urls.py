from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mangas/', views.mangas, name='mangas'),
    path('figuras/', views.figuras, name='figuras'),
    path('registro/', views.registro, name='registro'),
    path('listado-Mangakas/', views.listado_mangakas, name='listado_mangakas'),
    path('nuevo-mangaka/', views.crear_mangaka, name='crear_mangakas'),
    path('modificar-mangaka/<id>/', views.modificar_mangaka, name='modificar_mangaka'),
    path('eliminar-mangaka/<id>/', views.eliminar_mangaka, name='eliminar_mangaka'),
    path('listado-Mangas/', views.listado_mangas, name='listado_mangas'),
    path('nuevo-manga/', views.crear_mangas, name='crear_mangas'),
    path('modificar-manga/<id>/', views.modificar_mangas, name='modificar_mangas'),
    path('eliminar-manga/<id>/', views.eliminar_mangas, name='eliminar_mangas'),
    path('listado-Figuras/', views.listado_figuras, name='listado_figuras'),
    path('nuevo-figura/', views.crear_figuras, name='crear_figuras'),
    path('modificar-figura/<id>/', views.modificar_figura, name='modificar_figura'),
    path('eliminar-figura/<id>/', views.eliminar_figura, name='eliminar_figura'),
    path('contacto/' ,views.contacto, name='contacto'),
    path('listado-recetas/', views.listado_recetas, name='listado_recetas'),
    path('nueva-receta/', views.crear_recetas, name='nueva_receta'),
    path('modificar-recetas/<id>/', views.modificar_recetas, name='modificar_recetas'),
    path('eliminar-recetas/<id>/', views.eliminar_recetas, name='eliminar_recetas'),
]
urlpatterns +=[
  
]