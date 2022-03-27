from django.db import models

'''
Classe de modelagem do desafio, assim como requisitado.
Todos os campos tem os tamanhos e os tipos pedidos.
'''


# Classe de modelagem do problema

class Fornecedores(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=140)
    company = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    amount_products = models.IntegerField()

    def __str__(self):
        return self.name
