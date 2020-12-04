from django.shortcuts import render, redirect
from . models import Manga, Mangaka, Genero,Figuras,Marca
from django.views import generic
from .forms import MangakaForm,FigurasForm ,MangaForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )
def mangas(request):
    data = {
        'manga':Manga.objects.all()
    }

    return render(
        request,
        'mangas.html', data
       
    )
def figuras(request):
    data = {
        'figuras':Figuras.objects.all()
    }
    return render(
        request,
        'figuras.html', data
    )
def registro(request):
    return render(
        request,
        'registro.html'
    )
#mangakas#
def listado_mangakas(request):
    mangakas= Mangaka.objects.all()
    data = {
        'mangakas':mangakas
    }
    return render(
        request,
        'listado_mangakas.html',data
    )
def crear_mangaka(request):
    data = {
        'form' :MangakaForm()
    }

    if request.method == 'POST':
        formulario = MangakaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se ha creado un mangaka"

    return render(
        request,
        'nuevo_mangaka.html', data
    )
def modificar_mangaka(request, id):
    mangaka= Mangaka.objects.get(id=id)
    data = {
        'form':MangakaForm(instance=mangaka)
    }

    if request.method == 'POST':
        formulario = MangakaForm(data=request.POST, instance=mangaka)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] ='Modificado Correctamente'
            data['form'] = formulario
    return render (
        request,
        'modificar_mangaka.html',data
    )
def eliminar_mangaka(request, id):
    mangaka =Mangaka.objects.get(id=id)
    mangaka.delete()
    return redirect(to="listado_mangakas")
#Mangas#

def listado_mangas(request):
    manga= Manga.objects.all()
    data = {
        'manga':manga
    }
    return render(
        request,
        'lista_mangas.html',data
    )
def crear_mangas(request):
    data = {
        'form' :MangaForm()
    }

    if request.method == 'POST':
        formulario = MangaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se ha creado un manga"

    return render(
        request,
        'nuevo_manga.html', data
    )
def modificar_mangas(request, id):
    manga= Manga.objects.get(id=id)
    data = {
        'form':MangaForm(instance=manga)
    }

    if request.method == 'POST':
        formulario = MangaForm(data=request.POST, instance=manga, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] ='Modificado Correctamente'
            data['form'] = MangaForm(instance=Manga.objects.get(id=id))
    return render (
        request,
        'modificar_manga.html',data
    )
def eliminar_mangas(request, id):
    manga=Manga.objects.get(id=id)
    manga.delete()
    return redirect(to="listado_mangas")

##Figuras##
def listado_figuras(request):
    figuras= Figuras.objects.all()
    data = {
        'figuras':figuras
    }
    return render(
        request,
        'listado_figuras.html',data
    )
def crear_figuras(request):
    data = {
        'form' :FigurasForm()
    }

    if request.method == 'POST':
        formulario = FigurasForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se ha creado un mangaka"

    return render(
        request,
        'nuevo_figura.html', data
    )
def modificar_figura(request, id):
    figuras= Figuras.objects.get(id=id)
    data = {
        'form':FigurasForm(instance=figuras)
    }

    if request.method == 'POST':
        formulario = FigurasForm(data=request.POST, instance=figuras, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] ='Modificado Correctamente'
            data['form'] = FigurasForm(instance=Figuras.objects.get(id=id))
    return render (
        request,
        'modificar_figura.html',data
    )
def eliminar_figura(request, id):
    figuras =Figuras.objects.get(id=id)
    figuras.delete()
    return redirect(to="listado_figuras")

