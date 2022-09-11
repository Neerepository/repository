from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from tkinter.tix import Form
from tkinter.ttk import Widget
from unicodedata import category
from django import forms
from .models import *
from django.db.models import Q

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','categoria','subcategoria','link','image','videos']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
            'categoria': forms.Select(attrs={'class':'form-control', 'placeholder':'Categoria'}),
            'subcategoria':forms.CheckboxSelectMultiple(),
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Link'}),
           
        }
        labels = {
            'title':'','description':'','categoria':'','subcategoria':'','link':''
        }

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['categoria','subcategoria','description']
        widgets = {
            
            'categoria': forms.Select({'placeholder':'Seleccione una categoria'}),
            'subcategoria':forms.TextInput(attrs={'class':'form-control', 'placeholder':'SubCategoria'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'})
        
        }
        labels = {
            'categoria':'','subcategoria':'','description':''
        }

    
def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if Project.objects.filter(title=title).exists():
                raise forms.ValidationError("ya está registrado, prueba con otro.")
        return title


class VerificationForm(forms.Form):
    Template_name = 'use'