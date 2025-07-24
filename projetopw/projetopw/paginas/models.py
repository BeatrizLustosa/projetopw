from django.db import models
from django.contrib.auth.models import User

class Midia(models.Model):
    foto_perfil =  models.URLField(max_length=255)
    divulgacao_cantor = models.URLField(max_length=255)
    divulgacao_show = models.URLField(max_length=255)
    
    

class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome +  " - " + self.cidade 

class TipoShow (models.Model):
    tipo_show = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_show
    
class PerfilCantor(models.Model):
    nome_artistico =  models.CharField(max_length=100)
    genero_musical =  models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.URLField(max_length=255)
    telefone = models.CharField(max_length=20)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_cantor')
    
class Show(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField() 
    hora  = models.TimeField()
    local = models.ForeignKey(Local,on_delete=models.PROTECT)
    tipo_show = models.ForeignKey(TipoShow,on_delete=models.PROTECT)
    foto_show = models.URLField(max_length=100)

    def __str__(self):
        return  f"{self.nome} ({self.local}) ({self.tipo_show})"
        
