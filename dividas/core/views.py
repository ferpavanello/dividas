from dividas.core.models import Divida
from dividas.core.forms import DividaForm
from dividas.core.serializers import DividaSerializer
from rest_framework import generics
from django.shortcuts import render, resolve_url as r, get_object_or_404
from django.http import HttpResponseRedirect


class DividaList(generics.ListCreateAPIView):
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer


class DividaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer


def home(request, id_cliente=None):
    if id_cliente:
        dividas = Divida.objects.all().filter(id_cliente=id_cliente).order_by("data")
    else:
        dividas = Divida.objects.all().order_by("data")

    return render(request, 'index.html', dict(dividas=dividas))


def nova(request):
    print("!!!!!!!!!!!")
    form = DividaForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(r('dividas:home'))
    return render(request, 'nova.html', {'form': form})


def alterar(request, id):
    divida = get_object_or_404(Divida, id=id)
    form = DividaForm(request.POST or None, instance=divida)
    print("0")
    print(request)
    if request.POST:
        print("1")
        if form.is_valid():
            print("2")
            form.save()
            # return HttpResponseRedirect(r('dividas:home'))
    return render(request, 'nova.html', {'form': form})


def deletar(request, id):
    Divida.objects.filter(id=id).delete()
    return HttpResponseRedirect(r('dividas:home'))
