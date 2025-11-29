from django.contrib import admin
from django.contrib import admin
from .models import Show

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'hora', 'local') # Ajuste com os campos do seu model
    # O superusuário automaticamente pode editar e excluir aqui