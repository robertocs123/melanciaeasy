from django.db import models
from django.contrib.auth import get_user_model
class Preco(models.Model):
    rgrauda = models.FloatField(default = 1.00)
    rmedia = models.FloatField(default = 1.00)
    rmiuda = models.FloatField(default = 1.00)
    def __init__(self):
        return self.rmedia

class Pedido(models.Model):

    STATUS = (
        ('doing', 'Esperando pedido'),
        ('done', 'Pedido entregue'),
    )

    STATUSTIPO = (
        ('rgrauda', 'Redonda Graúda'),
        ('rmedia', 'Redonda Média'),
        ('rmiuda', 'Redonda Miúda'),

    )
    VALOR = 0.00
    STATUSVALOR = (
        (VALOR, 'Valor não disponível')
    
    )
    quantidade = models.IntegerField(default=1)
    vendedor = models.CharField(max_length=30, default='Roberto')
    tipomelancia = models.CharField(max_length=7,choices=STATUSTIPO)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    pontoreferencia = models.CharField(max_length=100)
    valor = models.FloatField(default = VALOR)
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )   
    comentario = models.TextField(max_length=200, default='Sem comentário')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipomelancia
