from django.db import models
from django.contrib.auth.models import User

# models.py

# ... (Seus imports)

class Midia(models.Model):
    # Relacionamento de Um-Para-Um com PerfilCantor
    # Se um PerfilCantor for deletado, as mídias associadas também serão.
    perfil = models.OneToOneField(
        'PerfilCantor', 
        on_delete=models.CASCADE, 
        related_name='midias'
    )
    foto_perfil = models.URLField(max_length=255)
    divulgacao_cantor = models.URLField(max_length=255)
    divulgacao_show = models.URLField(max_length=255)
    
    def __str__(self):
        # Para que apareça o nome do cantor no Admin/Debug
        return f"Mídias de {self.perfil.nome_artistico}"

# ... (Restante dos seus modelos)
    

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
    genero_musical =  models.CharField(max_length=100, null=True)
    descricao = models.TextField(null=True)
    foto = models.URLField(max_length=255, null=True)
    telefone = models.CharField(max_length=20)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_cantor')
    
class Show(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField() 
    hora  = models.TimeField()
    cantor = models.ForeignKey(User,on_delete=models.CASCADE)
    local = models.ForeignKey(Local,on_delete=models.PROTECT)
    tipo_show = models.ForeignKey(TipoShow,on_delete=models.PROTECT)
    foto_show = models.URLField(max_length=100)
    
    def __str__(self):
        return  f"{self.nome} ({self.local}) ({self.tipo_show})"
    
    class Meta:
        ordering = ['data']
        
