from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Local, TipoShow, Midia, Show, PerfilCantor
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

##############################################
#CREATE

class MidiaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = reverse_lazy('index')
    success_message = "Midia criada com sucesso!"
    extra_context = {'titulo' : 'Cadastro De Fotos',
                     'botao' : 'Salvar'}

class LocalCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Local
    fields = ['nome', 'endereco', 'cidade']
    success_url = reverse_lazy('index')
    success_message = "Local criado com sucesso!"
    extra_context = {'titulo' : 'Cadastro De Local',
                     'botao' : 'Salvar'}
                     
class TipoShowCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'paginas/form.html'
    model = TipoShow
    fields = ['tipo_show']
    success_url = reverse_lazy('index')
    success_message = "Tipo de Show criado com sucesso!"
    extra_context = {'titulo' : 'Cadastro do Tipo de Show',
                      'botao' : 'Salvar'}
    
class PerfilCantorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'paginas/form.html'
    model = PerfilCantor
    fields = ['nome_artistico', 'genero_musical', 'descricao', 'foto', 'telefone']
    success_url = reverse_lazy('index')
    success_message = "Perfil criado com sucesso!"
    extra_context = {'titulo' : 'Cadastro Do Cantor',
                     'botao' : 'Salvar'}
class ShowCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['nome', 'data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    success_message = "Show criado com sucesso!"
    extra_context = {'titulo' : 'Cadastro Do Show',
                     'botao' : 'Salvar'}
###############################################
#UPDATE

class MidiaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = reverse_lazy('index')
    success_message = "Midia Alterada com sucesso!"
    extra_context = {'titulo' : 'Atualização De Fotos',
                     'botao' : 'Salvar'}

class LocalUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Local
    fields = ['nome', 'endereco', 'cidade']
    success_url = reverse_lazy('index')
    success_message = "Local Alterado com sucesso!"
    extra_context = {'titulo' : 'Atualização de Local',
                     'botao' : 'Salvar'}
                     
class TipoShowUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = TipoShow
    fields = ['tipo_show']
    success_url = reverse_lazy('index')
    success_message = "Tipo de show Alterado com sucesso!"
    extra_context = {'titulo' : 'Atualização do Tipo de Show',
                      'botao' : 'Salvar'}
    
class PerfilCantorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = PerfilCantor
    fields = ['nome_artistico', 'genero_musical', 'descricao', 'foto', 'telefone']
    success_url = reverse_lazy('index')
    success_message = "Perfil Alterado com sucesso!"
    extra_context = {'titulo' : 'Atualização Do Cantor',
                     'botao' : 'Salvar'}
    
class ShowUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['nome', 'data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    success_message = "Show Alterado com sucesso!"
    extra_context = {'titulo' : 'Atualização Do Show',
                     'botao' : 'Salvar'}
##################################################
#DELETE
class MidiaDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Midia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    success_message = "Midia Excluída com sucesso!"
    extra_context = {'titulo': 'Excluir Midia',
                     'botao': 'Excluir'}
    

class LocalDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Local
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    success_message = "Local Excluído com sucesso!"
    extra_context = {'titulo': 'Excluir Local',
                     'botao': 'Excluir'}

class TipoShowDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TipoShow
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    success_message = "Tipo do Show Excluído com sucesso!"
    extra_context = {'titulo': 'Excluir TipoShow',
                     'botao': 'Excluir'}

class PerfilCantorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PerfilCantor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    success_message = "Perfil Excluído com sucesso!"
    extra_context = {'titulo': 'Excluir Cantor',
                     'botao': 'Excluir'}

class ShowDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Show
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    success_message = "Show Excluído com sucesso!"
    extra_context = {'titulo': 'Excluir Show',
                     'botao': 'Excluir'}

######################################################
class MidiaList(LoginRequiredMixin, ListView):
   model = Midia
   template_name = 'ver/midia.html'
    

class LocalList(LoginRequiredMixin, ListView):
    model = Local
    template_name = 'ver/local.html'

class TipoShowList(LoginRequiredMixin, ListView):
    model = TipoShow
    template_name = 'ver/tipo.html'
    

class PerfilCantorList(ListView):
    model = PerfilCantor
    template_name = 'ver/perfil.html'
    
class ShowList(ListView):
    model = Show
    template_name = 'ver/show.html'

###########################################

class CriarMidiaView(SuccessMessageMixin, CreateView):
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = '/midias/'
    success_message = "Mídia cadastrada com sucesso!"
