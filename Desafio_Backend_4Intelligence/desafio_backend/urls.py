"""desafio_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Fornecedores.api.viewsets import FornecedoresRead, FornecedoresCreate, FornecedoresUpdate, \
    FornecedoresDelete

router = routers.DefaultRouter()


# Os paths adicionados são os endpoints que permitem realizar o CRUD na API

urlpatterns = [
    path('', include(router.urls)),
    path(r'read', FornecedoresRead.as_view(),name='Read'),
    path(r'create', FornecedoresCreate.as_view(), name='create'),
    path(r'update/<str:id>/', FornecedoresUpdate.as_view(),name='FornecedorUpdate'),
    path(r'delete/<str:id>/', FornecedoresDelete.as_view(),name="delete"),
    path(r'admin/', admin.site.urls),
]
