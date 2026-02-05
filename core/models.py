from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Produto')
    descricao = models.TextField(verbose_name='Descrição do Produto')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço do Produto')
    estoque = models.IntegerField(verbose_name='Quantidade em Estoque')

    def __str__(self):
        return self.nome