from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from .models import *

class BlogForm(ModelForm):
    resenia = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Blog
        fields='__all__'
        labels={
            'titulo':"Título del film",
            'anio':"Fecha de lanzamiento (AAAA-MM-DD)",
            'duracion':"Duración en minutos",
            'genero':"Género",
            'imagen':"Portada",
            'subtitulo':"Título de reseña",
            'resenia':"Reseña",
            'estrellas':"Estrellas",
            'autor':"Autor de reseña",
            'fecha':"Fecha de publicación",
        }
        widgets={
            'autor':forms.TextInput(attrs={'readonly':'readonly'}),
            'fecha':forms.DateInput(attrs={'readonly':'readonly'}),
        }

class ComentarioForm(ModelForm):
    class Meta:
        model=Comentario
        fields=['texto', 'autor', 'fecha']
        labels={
            'texto':"Comentario",
            'autor':"Autor",
            'fecha':"Fecha",
        }
        widgets={
            'texto':forms.Textarea(),
            'autor':forms.TextInput(attrs={'readonly':'readonly'}),
            'fecha':forms.DateInput(attrs={'readonly':'readonly'})
        }