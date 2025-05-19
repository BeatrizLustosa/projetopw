
from django.urls import path
from .views import IndexView, SobreView
from .views import MidiaCreate, LocalCreate, TipoShowCreate, PerfilCantorCreate, ShowCreate
from .views import MidiaUpdate, LocalUpdate, TipoShowUpdate, PerfilCantorUpdate, ShowUpdate

from .views import MidiaDelete, LocalDelete, TipoShowDelete, PerfilCantorDelete, ShowDelete
urlpatterns = [
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
    path("editar/perfil/<int:pk>/", PerfilCantorUpdate.as_view(), name="editar-perfil"),
    path("editar/show/<int:pk>/", ShowUpdate.as_view(), name="editar-show"),

###########################################################################

      path("excluir/midia/<int:pk>/", MidiaDelete.as_view(), name = "excluir-midia"),
      path("excluir/local/<int:pk>/", LocalDelete.as_view(), name="excluir-local"),
      path("excluir/tipo/<int:pk>/", TipoShowDelete.as_view(), name = "excluir-tipo"),
      path("excluir/perfil/<int:pk>/", PerfilCantorDelete.as_view(), name="excluir-perfil"),
      path("excluir/show/<int:pk>/", ShowDelete.as_view(), name = "excluir-show"),
     

]
