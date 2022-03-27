from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView
from Fornecedores.models import Fornecedores
from .serializers import FornecedoresSerializer


# Classe responsável por realizar a criação de fornecedores, herda de uma generic view que permite realizar a operação

class FornecedoresCreate(CreateAPIView):
    queryset = Fornecedores.objects.all()

    serializer_class = FornecedoresSerializer


'''
Classe responsável por realizar a listagem/leitura de fornecedores, herda de uma generic view que permite realizar 
a operação 
'''


class FornecedoresRead(ListAPIView):
    queryset = Fornecedores.objects.all()# Acessando todos os objetos de fornecedores que foram adicionados

    serializer_class = FornecedoresSerializer  # Serializando os objetocs, ou seja, passando de python para JSON



# Classe responsável por realizar o update de fornecedores, herda de uma generic view que permite realizar a operação

class FornecedoresUpdate(RetrieveUpdateAPIView):

    queryset = Fornecedores.objects.all() # Acessando todos os objetos de fornecedores que foram adicionados

    serializer_class = FornecedoresSerializer # Serializando os objetos, ou seja, passando de python para JSON

    lookup_field = 'id' # Sobescrevendo a chave que é usada como padrão pelo DRF


# Classe responsável por realizar o delete de fornecedores, herda de uma generic view que permite realizar a operação

class FornecedoresDelete(RetrieveDestroyAPIView):

    queryset = Fornecedores.objects.all() # Acessando todos os objetos de fornecedores que foram adicionados

    serializer_class = FornecedoresSerializer # Serializando os objetocs, ou seja, passando de python para JSON

    lookup_field = 'id' # Sobescrevendo a chave que é usada como padrão pelo DRF
