from dividas.core.models import Divida
from dividas.core.forms import DividaForm
from dividas.core.serializers import DividaSerializer
from rest_framework import generics
from django.shortcuts import render, resolve_url as r
from django.http import HttpResponseRedirect


class DividaList(generics.ListCreateAPIView):
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer


class DividaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer


def home(request):
    dividas = Divida.objects.all().order_by("data")
    return render(request, 'index.html', dict(dividas=dividas))


def nova(request):
    form = DividaForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(r('dividas:home'))
    return render(request, 'nova.html', {'form': form})
