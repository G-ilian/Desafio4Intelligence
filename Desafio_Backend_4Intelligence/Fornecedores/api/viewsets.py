from functools import partial

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import permissions
from Fornecedores.models import Fornecedores
from rest_framework.response import Response
from .serializers import FornecedoresSerializer, FornecedorUpdateSerializer

'''
Configurando uma viewset, que será utilizada para a url.
Através do ModelViewSet e suas facilidades é possível realizar um CRUD para um model qualquer
'''


class FornecedoresViewSet(ModelViewSet):
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer


# Classe responsável por realizar a criação de fornecedores, herda de uma generic view que permite realizar a operação

class FornecedoresCreate(CreateAPIView):
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer

    def create(self, request, *args, **kwargs):
        return super(FornecedoresCreate, self).create(request, *args, **kwargs)


# Classe responsável por realizar a listagem/leitura de fornecedores, herda de uma generic view que permite realizar a operação

class FornecedoresRead(ListAPIView):
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer

    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        return super(FornecedoresRead, self).list(request, *args, **kwargs)


# Classe responsável por realizar o update de fornecedores, herda de uma generic view que permite realizar a operação

class FornecedoresUpdate(RetrieveUpdateAPIView):
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer
    lookup_field = 'id'


# Classe responsável por realizar o delete de fornecedores, herda de uma generic view que permite realizar a operação

class FornecedoresDelete(DestroyAPIView):
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer
    lookup_field = 'id'
