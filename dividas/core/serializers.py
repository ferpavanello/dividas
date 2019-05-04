from dividas.core.models import Divida
from rest_framework import serializers


class DividaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divida
        fields = '__all__'
