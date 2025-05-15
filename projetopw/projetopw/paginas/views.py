from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Local, TipoShow, Midia, Show, PerfilCantor
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

##############################################
#CREATE

class MidiaCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro De Fotos',
                     'botao' : 'Salvar'}

class LocalCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Local
    fields = ['nome', 'endereco', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro De Local',
                     'botao' : 'Salvar'}
                     
class TipoShowCreate(CreateView):
    template_name = 'paginas/form.html'
    model = TipoShow
    fields = ['tipo_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro do Tipo de Show',
                      'botao' : 'Salvar'}
    
class PerfilCantorCreate(CreateView):
    template_name = 'paginas/form.html'
    model = PerfilCantor
    fields = ['nome_artistico', 'genero_musical', 'descricao', 'foto', 'telefone']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro Do Cantor',
                     'botao' : 'Salvar'}
class ShowCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro Do Show',
                     'botao' : 'Salvar'}
###############################################
#UPDATE

class MidiaUpdade(UpdateView):
    template_name = 'paginas/form.html'
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização De Fotos',
                     'botao' : 'Salvar'}

class LocalUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Local
    fields = ['nome', 'endereco', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização de Local',
                     'botao' : 'Salvar'}
                     
class TipoShowUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = TipoShow
    fields = ['tipo_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização do Tipo de Show',
                      'botao' : 'Salvar'}
    
class PerfilCantorUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = PerfilCantor
    fields = ['nome_artistico', 'genero_musical', 'descricao', 'foto', 'telefone']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização Do Cantor',
                     'botao' : 'Salvar'}
    
class ShowUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização Do Show',
                     'botao' : 'Salvar'}
##################################################
#DELETE
