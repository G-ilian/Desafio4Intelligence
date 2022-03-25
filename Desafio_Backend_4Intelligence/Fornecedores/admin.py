from django.contrib import admin
from .models import Fornecedores

#Registrando os fornecedores na app.
#Pode ser acessado através de um super usuário.
admin.site.register(Fornecedores)