from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Local, TipoShow, Midia, Show, PerfilCantor
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

##############################################
#CREATE

class MidiaCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro De Fotos',
                     'botao' : 'Salvar'}

class LocalCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Local
    fields = ['nome', 'endereco', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro De Local',
                     'botao' : 'Salvar'}
                     
class TipoShowCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = TipoShow
    fields = ['tipo_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro do Tipo de Show',
                      'botao' : 'Salvar'}
    
class PerfilCantorCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = PerfilCantor
    fields = ['nome_artistico', 'genero_musical', 'descricao', 'foto', 'telefone']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro Do Cantor',
                     'botao' : 'Salvar'}
class ShowCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['nome', 'data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro Do Show',
                     'botao' : 'Salvar'}
###############################################
#UPDATE

class MidiaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização De Fotos',
                     'botao' : 'Salvar'}

class LocalUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Local
    fields = ['nome', 'endereco', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização de Local',
                     'botao' : 'Salvar'}
                     
class TipoShowUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = TipoShow
    fields = ['tipo_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização do Tipo de Show',
                      'botao' : 'Salvar'}
    
class PerfilCantorUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = PerfilCantor
    fields = ['nome_artistico', 'genero_musical', 'descricao', 'foto', 'telefone']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização Do Cantor',
                     'botao' : 'Salvar'}
    
class ShowUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['nome', 'data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Atualização Do Show',
                     'botao' : 'Salvar'}
##################################################
#DELETE
class MidiaDelete(LoginRequiredMixin, DeleteView):
    model = Midia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Midia',
                     'botao': 'Excluir'}
    

class LocalDelete(LoginRequiredMixin, DeleteView):
    model = Local
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Local',
                     'botao': 'Excluir'}

class TipoShowDelete(LoginRequiredMixin, DeleteView):
    model = TipoShow
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir TipoShow',
                     'botao': 'Excluir'}

class PerfilCantorDelete(LoginRequiredMixin, DeleteView):
    model = PerfilCantor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Cantor',
                     'botao': 'Excluir'}

class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Show
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Excluir Show',
                     'botao': 'Excluir'}

######################################################
class Midia(LoginRequiredMixin, ListView):
   model = Midia
   template_name = 'ver/show.html'
    

class Local(LoginRequiredMixin, ListView):
    model = Local
    template_name = 'ver/local.html'

class TipoShow(LoginRequiredMixin, ListView):
    model = TipoShow
    template_name = 'ver/tipo.html'
    

class PerfilCantor(ListView):
    model = PerfilCantor
    template_name = 'ver/perfil.html'
    
class Show(ListView):
    model = Show
    template_name = 'ver/show.html'

###########################################
   