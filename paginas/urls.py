
from django.urls import path
from .views import IndexView, SobreView
from .views import MidiaCreate, LocalCreate, TipoShowCreate, PerfilCantorCreate, ShowCreate
from .views import MidiaUpdate, LocalUpdate, TipoShowUpdate, PerfilCantorUpdate, ShowUpdate

from .views import MidiaDelete, LocalDelete, TipoShowDelete, PerfilCantorDelete, ShowDelete
from .views import MidiaList, LocalList, TipoShowList, PerfilCantorList, ShowList

from .views import CadastroUsuarioView


from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),

    path("login/", auth_views.LoginView.as_view(
        
         template_name = 'paginas/form.html',
          extra_context = {'titulo' : 'Autenticação',
                            'botao' : 'Entrar'}
    ), name="login"),


     path("senha/", auth_views.PasswordChangeView.as_view(
         template_name = 'paginas/form.html',
          extra_context = {'titulo' : 'Atualizar senha',
                            'botao' : 'Salvar'}
    ), name="senha"),

    path("sair/", auth_views.LogoutView.as_view(), name="sair"),
  
  
    path("senha/", auth_views.PasswordChangeView.as_view( 
         template_name = 'paginasweb/form.html',
         extra_context = {
             'titulo': 'Atualizar senha',
             'botao' : 'Salvar',
         }
    ),name="alterar-senha"),



    path("", IndexView.as_view(), name = "index"),
    path("sobre/", SobreView.as_view(), name = "sobre"),

###########################################################################

    path("inserir/midia/", MidiaCreate.as_view(), name="inserir-midia"),
    path("inserir/local/", LocalCreate.as_view(), name = "inserir-local"),
    path("inserir/tipo/", TipoShowCreate.as_view(), name="inserir-tipo"),
    path("inserir/perfil/", PerfilCantorCreate.as_view(), name="inserir-perfil"),
    path("inserir/show/", ShowCreate.as_view(), name="inserir-show"),

###########################################################################

    path("editar/midia/<int:pk>/", MidiaUpdate.as_view(), name="editar-midia"),
    path("editar/local/<int:pk>/", LocalUpdate.as_view(), name = "editar-local"),
    path("editar/tipo/<int:pk>/", TipoShowUpdate.as_view(), name="editar-tipo"),
    path("editar/perfil/", PerfilCantorUpdate.as_view(), name="editar-perfil"),
    path("editar/show/<int:pk>/", ShowUpdate.as_view(), name="editar-show"),

###########################################################################

    path("excluir/midia/<int:pk>/", MidiaDelete.as_view(), name = "excluir-midia"),
    path("excluir/local/<int:pk>/", LocalDelete.as_view(), name="excluir-local"),
    path("excluir/tipo/<int:pk>/", TipoShowDelete.as_view(), name = "excluir-tipo"),
    path("excluir/perfil/", PerfilCantorDelete.as_view(), name="excluir-perfil"),
    path("excluir/show/<int:pk>/", ShowDelete.as_view(), name = "excluir-show"),
     
###############################################################################
    
    path("ver/midia/", MidiaList.as_view(), name = "ver-midia"),
    path("ver/local/", LocalList.as_view(), name="ver-local"),
    path("ver/tipo/", TipoShowList.as_view(), name = "ver-tipo"),
    path("ver/perfil/", PerfilCantorList.as_view(), name="ver-perfil"),
    path("ver/show/", ShowList.as_view(), name = "ver-show"),
]
