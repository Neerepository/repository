from itertools import count
from django.db.models import Q, Count
from django.db import models

class PerfilMAnager(models.Manager):
    def buscar_perfiles(self, Kword):
        consulta = self.filter(
            Q(usar__icontains=Kword)
        )
        return consulta 