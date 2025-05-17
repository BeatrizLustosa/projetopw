from django.db import models

class Midia(models.Model):
    foto_perfil =  models.URLField(max_length=255)
    divulgacao_cantor = models.URLField(max_length=255)
    divulgacao_show = models.URLField(max_length=255)

class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

class TipoShow (models.Model):
    tipo_show = models.CharField(max_length=100)

class PerfilCantor(models.Model):
    nome_artistico =  models.CharField(max_length=100)
    genero_musical =  models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.URLField(max_length=255)
    telefone = models.CharField(max_length=20)
    
class Show(models.Model):
    data = models.DateField() 
    hora  = models.TimeField()
    local = models.ForeignKey(Local,on_delete=models.PROTECT)
    tipo_show = models.ForeignKey(TipoShow,on_delete=models.PROTECT)
    foto_show = models.URLField(max_length=100)
