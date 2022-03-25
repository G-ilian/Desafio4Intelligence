#Classe que tem como funcionalidade informar para a minha viewset como eu quero que o JSON seja organizado
from rest_framework.serializers import ModelSerializer
from Fornecedores.models import Fornecedores

class FornecedoresSerializer(ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = ('id', 'name', 'company', 'created_at', 'amount_products')