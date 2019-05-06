from django.urls import path
from dividas.core.views import DividaList, DividaDetail, home, nova, alterar, deletar

app_name = 'dividas'

urlpatterns = [
    path('', home, name='home'),
    path('<int:id_cliente>', home, name='home'),
    path('nova/', nova, name='nova-divida'),
    path('alterar/<int:id>', alterar, name='alterar-divida'),
    path('deletar/<int:id>', deletar, name='deletar-divida'),
    path('dividas/', DividaList.as_view(), name='dividas-list'),
    path('dividas/<int:pk>/', DividaDetail.as_view(), name='dividas-detail'),
]
