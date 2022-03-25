from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from Fornecedores.models import Fornecedores
from .serializers import FornecedoresSerializer
'''
Configurando uma viewset, que será utilizada para a url.
Através do ModelViewSet e suas facilidades é possível realizar um CRUD para um model qualquer
'''

class FornecedoresViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer
