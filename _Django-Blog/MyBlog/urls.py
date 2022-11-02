from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.noticia, name='noticia'),
    path('selecao/', views.selecao, name='selecao'),
    path('brasileirao/', views.brasileirao, name='brasileirao'),
    path('sobre/', views.sobre, name='sobre'),
]
