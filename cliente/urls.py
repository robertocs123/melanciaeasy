from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.pedidoList, name='pedido-list'),
    path('pedido/<int:id>', views.pedidoView, name="pedido-view"),
    path('newpedido/', views.newPedido, name="new-pedido"),
    path('sobre/', views.sobre, name="sobre"),
    path('precos/', views.precos, name="precos"),
    path('fotos/', views.fotos, name="fotos"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('edit/<int:id>', views.editPedido, name="edit-pedido"),
    path('delete/<int:id>', views.deletePedido, name="delete-pedido"),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]