
from django.urls import path
from .views import IndexView, SobreView
from .views import LocalCreate, TipoShowCreate, LocalUpdate, TipoShowUpdate
from .views import LocalUpdate, TipoShowUpdate
# from .views import LocalDelete, TipoShowDelete
urlpatterns = [
    path("", IndexView.as_view(), name = "index"),
    path("sobre/", SobreView.as_view(), name = "sobre"),

###########################################################################
    path("inserir/local/", LocalCreate.as_view(), name = "inserir-local"),
    path("inserir/tipo/", TipoShowCreate.as_view(), name="inserir-tipo"),

###########################################################################
    path("editar/local/<int:pk>/", LocalUpdate.as_view(), name = "editar-local"),
    path("editar/tipo/<int:pk>/", TipoShowUpdate.as_view(), name="editar-tipo"),

###########################################################################
    #  path("excluir/local/<int:pk>/", LocalDelete.as_view(), name = "excluir-local"),
    #  path("excluir/tipo/<int:pk>/", TipoShowDelete.as_view(), name="excluir-tipo"),


]
