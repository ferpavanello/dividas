from django import forms
from dividas.core.models import Divida


class DividaForm(forms.ModelForm):
    id_cliente = forms.CharField(
        label="Cliente", max_length=10, required=True)
    motivo = forms.CharField(
        label="Motivo", max_length=100, required=True, strip=True)
    valor = forms.DecimalField(
        label="Valor", max_digits=10, decimal_places=2, required=True)
    data = forms.DateField(label="Data", required=True)

    class Meta:
        model = Divida
        fields = '__all__'
