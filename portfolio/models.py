from dataclasses import field
from distutils.command.build import build
from distutils.command.upload import upload
from msilib.schema import Class
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from turtle import title, update
from unicodedata import category
from venv import create
from django.db import models
from .managers import CategoriaManager, ProjectManager
from django.contrib.auth.models import User


class Category(models.Model):
    category =  models.CharField(max_length=200, verbose_name="Categoria")
    
    class Meta: 
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
       
       # ordering = ["-created"]
    
    def __str__(self):
        return str(self.category)

    

# Create your models here.

class SubCategory(models.Model):
    subcategoria=models.CharField(max_length=200, verbose_name="SubCategoria")
    categoria= models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Descripcion")

    class Meta: 
        verbose_name = "subcategoria"
        verbose_name_plural = "subcategorias"
       
       # ordering = ["-created"]
    
    def __str__(self):
        return str(self.subcategoria)+ ' - ' + str(self.categoria)

class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    categoria= models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategoria =  models.ManyToManyField(SubCategory) 
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link= models.URLField (verbose_name="Link de Descarga",null=True, blank=True)
    videos= models.FileField (verbose_name="Video Tutorial",blank=True,null=True,  upload_to="projects" )
    likes = models.ManyToManyField(User, blank=True, related_name='likes' )
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes' )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    objects = ProjectManager()

    class Meta: 
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
       # ordering = ["-comments_Project__likes"]
       
       # ordering = ["-likes"]
    
    def __str__(self):
        return self.title + ' - ' + str(self.categoria)
