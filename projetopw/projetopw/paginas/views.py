from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Local, TipoShow
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class LocalCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Local
    fields = ['nome', 'endereco', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro De Local'}
    
class TipoShowCreate(CreateView):
    template_name = 'paginas/form.html'
    model = TipoShow
    fields = ['tipo_show']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastro do Tipo de Show'}