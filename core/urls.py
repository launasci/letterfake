from django.urls import path

from . import views

urlpatterns = [
    path('dapau', views.dapau),
    path('login', views.login),
    path('logout', views.logout),
    path('whoami', views.whoami),
    path('cadastro', views.cadastro),

    path("letterboxd/filmes", views.filmes),
    path("letterboxd/adicionar", views.adicionar_filmes),
    path("letterboxd/filme/<int:id>", views.pegar_filme),
    path("letterboxd/editar/<int:id>", views.editar_filme),
    path("letterboxd/excluir/<int:id>", views.excluir_filme)
]
