from django import forms
from django.forms import ModelForm
from .models import Mangaka, Manga , Figuras

class MangakaForm(ModelForm):

    class Meta:
        model = Mangaka
        fields = '__all__'
class MangaForm(ModelForm):

    class Meta:
        model = Manga
        fields = '__all__'
class FigurasForm(ModelForm):

    class Meta:
        model = Figuras
        fields = '__all__'
