
from django.urls import path
from .views import IndexView, SobreView
from .views import LocalCreate, TipoShowCreate

urlpatterns = [
    path("index/", IndexView.as_view(), name = "index"),
    path("sobre/", SobreView.as_view(), name = "sobre"),

    path("cadastrarlocal/", LocalCreate.as_view(), name = "inserir-local"),
    path("adicionartipo/", TipoShowCreate.as_view(), name="inserir-curso"),

]
