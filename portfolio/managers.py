from itertools import count
from django.db.models import Q, Count
from django.db import models


class ProjectManager (models.Manager):

    def buscar_herramienta(self, buscar):
        resultado = self.filter(
            Q(title__icontains=buscar) | Q(categoria__icontains=buscar)
        )
        return resultado 

    def add_autor_subcategoria(self, subcategoria,  categoria):
        libro = self.get(id=subcategoria)
        libro.category.add(categoria)
        return libro

class CategoriaManager(models.Manager):
    """ managers para el modelo autor """

    def categoria_por_herramienta(self, title):
        return self.filter(
            project_categoria__autores__id=title
        ).distinct()
