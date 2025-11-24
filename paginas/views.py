from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Local, TipoShow, Midia, Show, PerfilCantor
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm
from django.shortcuts import get_object_or_404

from django.db.models import Q 


class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qntd_show"] = Show.objects.all().count()
      
        return context
    
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'



# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': 'Cadastro de Usuário',
        'botao': 'Cadastrar', }


    def form_valid(self, form):
        nome_artistico = form.cleaned_data.get('nome_artistico')
        telefone = form.cleaned_data.get('telefone')
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Cantor')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)

        # Cria o perfil do cantor associado ao usuário
        PerfilCantor.objects.create(   
            usuario=self.object,
            nome_artistico=nome_artistico,
            telefone=telefone
        )
        # Retorna a URL de sucesso
        return url

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
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user  # 🔥 Atribui o usuário logado
        return super().form_valid(form)
    
class ShowCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['nome', 'data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    success_message = "Show criado com sucesso!"
    extra_context = {'titulo' : 'Cadastro Do Show',
                     'botao' : 'Salvar'}
    
    def form_valid(self, form):
        form.instance.cantor = self.request.user
        url = super().form_valid(form)
        return url
    

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
                     
    def get_object(self, queryset=None):
        obj = get_object_or_404(PerfilCantor, usuario=self.request.user)
        return obj
   

    
class ShowUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'paginas/form.html'
    model = Show
    fields = ['nome', 'data', 'hora', 'local', 'tipo_show', 'foto_show']
    success_url = reverse_lazy('index')
    success_message = "Show Alterado com sucesso!"
    extra_context = {'titulo' : 'Atualização Do Show',
                     'botao' : 'Salvar'}

    def get_object(self, queryset=None):
        obj = get_object_or_404(Show, pk=self.kwargs['pk'], cantor=self.request.user)
        return obj
    
    

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

    def get_object(self, queryset=None):
        obj = get_object_or_404(PerfilCantor, usuario=self.request.user)
        return obj

class ShowDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Show
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    success_message = "Show Excluído com sucesso!"
    extra_context = {'titulo': 'Excluir Show',
                     'botao': 'Excluir'}
                     

    def get_object(self, queryset=None):
        obj = get_object_or_404(Show, pk=self.kwargs['pk'], cantor=self.request.user)
        return obj
        
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

    def get_queryset(self):
        qs = PerfilCantor.objects.all()

        nome = self.request.GET.get("nome")

        if nome:
            qs = qs.filter(nome_artistico__icontains=nome)

        # ✔ Sempre ordenar alfabeticamente
        return qs.order_by("nome_artistico")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = self.request.GET.get("nome", "")
        return context



class ShowList(ListView):
    model = Show
    template_name = 'ver/show.html'
    
    def get_queryset(self):
        # 1. Ordenação Padrão: Pela data e hora mais próximas
        queryset = super().get_queryset().order_by('data', 'hora')
        
        cantor_busca = self.request.GET.get('cantor')
        ordenar_por = self.request.GET.get('ordenar_por')

        # 2. FILTRO POR CANTOR (Nome Artístico) 🎤
        if cantor_busca:
            # CORREÇÃO APLICADA: Usando cantor__perfil_cantor (com underscore)
            queryset = queryset.filter(
                Q(cantor__perfil_cantor__nome_artistico__icontains=cantor_busca) |
                Q(cantor__username__icontains=cantor_busca)
            )

        # 3. ORDENAÇÃO 🔠
        if ordenar_por == 'cantor_asc':
            # CORREÇÃO APLICADA: Usando cantor__perfil_cantor (com underscore)
            queryset = queryset.order_by('cantor__perfil_cantor__nome_artistico')
        elif ordenar_por == 'local_asc':
            queryset = queryset.order_by('local__nome')
        
        return queryset

    # ... get_context_data permanece igual
    def get_context_data(self, **kwargs):
        # Passa os parâmetros GET para o template para manter o formulário preenchido
        context = super().get_context_data(**kwargs)
        context['filtros_aplicados'] = self.request.GET
        return context

###########################################

class CriarMidiaView(SuccessMessageMixin, CreateView):
    model = Midia
    fields = ['foto_perfil', 'divulgacao_cantor', 'divulgacao_show']
    success_url = '/midias/'
    success_message = "Mídia cadastrada com sucesso!"
