from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('minha_consulta', views.revisao_consulta, name='minha_consulta')
]