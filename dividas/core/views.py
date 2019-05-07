from dividas.core.models import Divida
from dividas.core.serializers import DividaSerializer
from rest_framework import generics
from django.shortcuts import render


class DividaList(generics.ListCreateAPIView):
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer


class DividaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer


def home(request, id_cliente=None):
    return render(request, 'index.html')


def nova(request):
    return render(request, 'nova.html')


def alterar(request, id):
    return render(request, 'altera.html')
