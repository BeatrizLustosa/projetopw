from django.db import models

# Create your models here.

class Local (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

class TipoShow (models.Model):
    tipo_show = models.CharField(max_length=100)
